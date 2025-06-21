import itertools
from typing import List, Tuple

try:
    import networkx as nx
    import pymetis
except ImportError as e:
    nx = None
    pymetis = None


class Hypergraph:
    """Simple hypergraph representation."""

    def __init__(self, num_vertices: int, hyperedges: List[List[int]]):
        self.num_vertices = num_vertices
        self.hyperedges = hyperedges

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

            hyperedges = []
            for _ in range(num_edges):
                tokens = f.readline().strip().split()
                if e_weighted:
                    tokens = tokens[1:]
                hyperedges.append([int(t) - 1 for t in tokens])
            # vertex weights are ignored for now
        return cls(num_vertices, hyperedges)

    def to_graph(self):
        """Convert the hypergraph to a NetworkX graph using clique expansion."""
        if nx is None:
            raise ImportError("networkx is required for graph conversion")
        G = nx.Graph()
        G.add_nodes_from(range(self.num_vertices))
        for hedge in self.hyperedges:
            for u, v in itertools.combinations(hedge, 2):
                if G.has_edge(u, v):
                    G[u][v]["weight"] += 1
                else:
                    G.add_edge(u, v, weight=1)
        return G


def spectral_partition(graph, nparts: int = 2) -> Tuple[List[int], float]:
    """Partition a NetworkX graph using a simple spectral algorithm."""
    if nx is None:
        raise ImportError("networkx is required for spectral partitioning")
    try:
        import numpy as np
    except ImportError as e:
        raise ImportError("numpy is required for spectral partitioning") from e

    if nparts != 2:
        raise NotImplementedError("Only bipartitioning is supported")

    A = nx.to_numpy_array(graph, nodelist=range(graph.number_of_nodes()), weight="weight")
    degs = A.sum(axis=1)
    L = np.diag(degs) - A
    eigvals, eigvecs = np.linalg.eigh(L)
    idx = eigvals.argsort()[1]
    fiedler = eigvecs[:, idx]
    parts = [0 if x <= 0 else 1 for x in fiedler]

    # compute cut value for reference
    cut = 0.0
    for u, v, w in graph.edges(data="weight", default=1):
        if parts[u] != parts[v]:
            cut += w
    return parts, cut


def metis_partition(graph, nparts: int) -> Tuple[List[int], int]:
    """Partition a NetworkX graph using PyMetis."""
    if pymetis is None:
        raise ImportError("pymetis is required for partitioning")
    adj_list = [list(graph.neighbors(v)) for v in range(graph.number_of_nodes())]
    cuts, part = pymetis.part_graph(nparts, adjacency=adj_list)
    return part, cuts


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
