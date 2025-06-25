"""Port of `HypergraphToIncidence.jl`."""
from typing import List
from .pyspecpart import Incidence


def hypergraph_to_incidence(H) -> Incidence:
    """Convert a hypergraph to incidence representation."""
    hedges: List[int] = []
    eptr: List[int] = [0]
    d = [0] * H.num_vertices
    for v in range(H.num_vertices):
        edges = [i for i, e in enumerate(H.hyperedges) if v in e]
        hedges.extend(edges)
        eptr.append(len(hedges))
        d[v] = sum(H.hyperedge_weights[i] for i in edges)
    return Incidence(H.num_vertices, len(H.hyperedges), hedges, eptr, d)
