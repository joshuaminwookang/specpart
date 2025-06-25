"""Generate a graph weighted by eigenvector magnitudes."""

from typing import Any


def generateeigenawaregraph(graph: Any, eigenvector) -> Any:
    if hasattr(graph, "edges"):
        import networkx as nx  # type: ignore

        G = nx.Graph()
        for u, v in graph.edges():
            w = abs(eigenvector[u] - eigenvector[v])
            G.add_edge(u, v, weight=w)
        return G

    adj = {}
    for u, nbrs in graph.items():
        adj[u] = {v: abs(eigenvector[u] - eigenvector[v]) for v in nbrs}
    return adj

