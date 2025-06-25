"""Simplified iterative spectral partitioning."""

from typing import List


def iterative_spectral(hypergraph, iterations: int = 3) -> List[int]:
    """Repeatedly apply :func:`spectral_partition` to the hypergraph."""

    from .pyspecpart import spectral_partition

    G = hypergraph.to_graph()
    parts = [0] * hypergraph.num_vertices
    for _ in range(max(1, iterations)):
        parts, _ = spectral_partition(G, 2)
    return parts

