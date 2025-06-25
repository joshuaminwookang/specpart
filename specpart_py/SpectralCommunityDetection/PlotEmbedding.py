"""Return a planar embedding using the spring layout."""

from typing import Any, Dict


def plotembedding(graph: Any) -> Dict[int, tuple]:
    if hasattr(graph, "number_of_nodes"):
        import networkx as nx  # type: ignore

        return nx.spring_layout(graph, seed=0)

    # approximate layout for adjacency dict
    n = len(graph)
    return {i: (i % n, i // n) for i in range(n)}

