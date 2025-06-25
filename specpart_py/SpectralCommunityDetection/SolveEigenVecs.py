"""Compute eigenvectors of the Laplacian of a graph."""

from typing import Any, Tuple


def solveeigenvecs(graph: Any, k: int = 2) -> Tuple[list, list]:
    import numpy as np
    from ..pyspecpart import Hypergraph

    if hasattr(graph, "edges"):
        import networkx as nx  # type: ignore
        A = nx.to_numpy_array(graph, nodelist=range(graph.number_of_nodes()))
    else:
        n = len(graph)
        A = np.zeros((n, n))
        for u, nbrs in graph.items():
            for v in nbrs:
                A[u, v] = 1
                A[v, u] = 1

    D = np.diag(A.sum(axis=1))
    L = D - A
    vals, vecs = np.linalg.eigh(L)
    idx = np.argsort(vals)[:k]
    return vals[idx].tolist(), vecs[:, idx].tolist()

