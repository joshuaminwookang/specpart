"""Compute a simple unweighted Laplacian for a hypergraph."""

from typing import Any


def hypl(hypergraph: Any):
    import numpy as np

    n = hypergraph.num_vertices
    L = np.zeros((n, n))
    for hedge in hypergraph.hyperedges:
        for u in hedge:
            L[u, u] += 1
        for i, u in enumerate(hedge):
            for v in hedge[i + 1 :]:
                L[u, v] -= 1
                L[v, u] -= 1
    return L

