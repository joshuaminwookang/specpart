import itertools
from dataclasses import dataclass
from typing import List, Tuple, Optional

try:
    import networkx as nx  # type: ignore
except Exception:
    nx = None
try:
    import pymetis  # type: ignore
except Exception:
    pymetis = None


@dataclass
class Hypergraph:
    """Simple hypergraph representation with optional weights."""

    num_vertices: int
    hyperedges: List[List[int]]
    vertex_weights: List[int]
    hyperedge_weights: List[int]
    hedges: List[int]
    eptr: List[int]

    def __init__(self, num_vertices: int, hyperedges: List[List[int]],
                 vertex_weights: Optional[List[int]] = None,
                 hyperedge_weights: Optional[List[int]] = None):
        self.num_vertices = num_vertices
        self.hyperedges = hyperedges
        self.vertex_weights = vertex_weights or [1] * num_vertices
        self.hyperedge_weights = hyperedge_weights or [1] * len(hyperedges)

        self.hedges = []
        self.eptr = [0]
        for e in hyperedges:
            self.hedges.extend(e)
            self.eptr.append(len(self.hedges))

    @classmethod
    def from_hgr(cls, path: str) -> "Hypergraph":
        """Read a hypergraph in hMetis .hgr format."""
        with open(path) as f:
            first = f.readline().strip()
            parts = first.split()
            num_edges = int(parts[0])
            num_vertices = int(parts[1])
            mode = int(parts[2]) if len(parts) > 2 else 0
            e_weighted = mode % 10 == 1

            hyperedges: List[List[int]] = []
            edge_wts: List[int] = []
            for _ in range(num_edges):
                tokens = f.readline().strip().split()
                if e_weighted:
                    edge_wts.append(int(tokens[0]))
                    tokens = tokens[1:]
                else:
                    edge_wts.append(1)
                hyperedges.append([int(t) - 1 for t in tokens])

            vertex_wts: List[int] = [1] * num_vertices
            if mode >= 10:
                for i in range(num_vertices):
                    line = f.readline()
                    if line is None:
                        break
                    vertex_wts[i] = int(line.strip())

        return cls(num_vertices, hyperedges, vertex_wts, edge_wts)

    def to_graph(self):
        """Convert the hypergraph to a simple adjacency structure."""
        if nx is not None:
            G = nx.Graph()
            G.add_nodes_from(range(self.num_vertices))
            for hedge in self.hyperedges:
                for u, v in itertools.combinations(hedge, 2):
                    if G.has_edge(u, v):
                        G[u][v]["weight"] += 1
                    else:
                        G.add_edge(u, v, weight=1)
            return G

        # lightweight adjacency dictionary fallback
        adj = {i: set() for i in range(self.num_vertices)}
        for hedge in self.hyperedges:
            for u, v in itertools.combinations(hedge, 2):
                adj[u].add(v)
                adj[v].add(u)
        return adj


def spectral_partition(graph, nparts: int = 2) -> Tuple[List[int], float]:
    """Simple spectral-like partitioning without heavy dependencies."""
    if nparts != 2:
        raise NotImplementedError("Only bipartitioning is supported")

    if nx is not None and hasattr(graph, "edges"):
        import numpy as np  # type: ignore
        A = nx.to_numpy_array(graph, nodelist=range(graph.number_of_nodes()), weight="weight")
        degs = A.sum(axis=1)
        L = np.diag(degs) - A
        eigvals, eigvecs = np.linalg.eigh(L)
        idx = eigvals.argsort()[1]
        fiedler = eigvecs[:, idx]
        parts = [0 if x <= 0 else 1 for x in fiedler]
        cut = 0.0
        for u, v, w in graph.edges(data="weight", default=1):
            if parts[u] != parts[v]:
                cut += w
        return parts, cut

    # fallback using BFS ordering
    n = len(graph)
    order = []
    visited = [False] * n
    from collections import deque

    dq = deque([0])
    visited[0] = True
    while dq:
        v = dq.popleft()
        order.append(v)
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                dq.append(w)

    parts = [0] * n
    for i, v in enumerate(order):
        if i >= n // 2:
            parts[v] = 1

    cut = 0
    for u in range(n):
        for v in graph[u]:
            if u < v and parts[u] != parts[v]:
                cut += 1
    return parts, float(cut)


def metis_partition(graph, nparts: int) -> Tuple[List[int], int]:
    """Partition a graph using PyMetis if available, otherwise a simple heuristic."""
    if pymetis is not None and hasattr(graph, "neighbors"):
        adj_list = [list(graph.neighbors(v)) for v in range(graph.number_of_nodes())]
        cuts, part = pymetis.part_graph(nparts, adjacency=adj_list)
        return part, cuts

    # fallback: use spectral partition
    parts, cut = spectral_partition(graph, nparts)
    return parts, int(cut)


def partition_hgr(path: str, nparts: int = 2) -> List[int]:
    """Partition a hypergraph using PyMetis with clique expansion."""
    hg = Hypergraph.from_hgr(path)
    G = hg.to_graph()
    part, _ = metis_partition(G, nparts)
    return part


def spectral_partition_hgr(path: str, nparts: int = 2) -> List[int]:
    """Partition a hypergraph using the spectral method."""
    hg = Hypergraph.from_hgr(path)
    G = hg.to_graph()
    part, _ = spectral_partition(G, nparts)
    return part


@dataclass
class Incidence:
    """Incidence structure of a hypergraph."""

    n: int
    e: int
    hedges: List[int]
    eptr: List[int]
    d: List[int]


@dataclass
class HypergraphC:
    """Container bundling hypergraph and auxiliary information."""

    HG: Hypergraph
    incidence_list: List[List[int]]
    hyperedges_pair_list: List[Tuple[int, int]]
    community: List[int]
    fixed_part: List[int]
    fixed_vertex_flag: bool
    hyperedges_hash: dict


# utility functions are imported from helper modules
from .GenerateHyperedgesHash import generate_hyperedges_hash
from .HypergraphToIncidence import hypergraph_to_incidence
from .HypergraphToPairList import generate_hypergraph_pair_list
from .GenerateCoarseHypergraph import generate_coarse_hypergraph
from .InitialPartitions import generate_random_initial_partitions
from .ExportHypergraph import export_hypergraph
from .WriteClusters import write_clusters
from .StructureDetection import structure_detection
from .Coarsen import coarsen_hypergraph
from .Uncoarsen import uncoarsen_hypergraph
from .FM import fm
from .PartitionILP import partition_ilp
from .SpectralRefinement import spectral_refinement
from .EstimateClusteringMistakes import estimate_clustering_mistakes


def generate_incidence_list(B: Incidence) -> List[List[int]]:
    """Return incidence list from incidence structure."""
    res = []
    for i in range(B.n):
        res.append(B.hedges[B.eptr[i]:B.eptr[i + 1]])
    return res

