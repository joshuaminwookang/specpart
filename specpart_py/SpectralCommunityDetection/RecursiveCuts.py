"""Recursively bisect a graph using spectral partitioning."""

from typing import Any, List


def recursivecuts(graph: Any, depth: int = 1) -> List[List[int]]:
    from ..pyspecpart import spectral_partition

    if depth <= 0 or (hasattr(graph, "number_of_nodes") and graph.number_of_nodes() <= 2):
        if hasattr(graph, "nodes"):
            return [list(graph.nodes())]
        return [list(graph.keys())]

    parts, _ = spectral_partition(graph, 2)

    if hasattr(graph, "subgraph"):
        import networkx as nx  # type: ignore
        part0 = [v for v, p in enumerate(parts) if p == 0]
        part1 = [v for v, p in enumerate(parts) if p == 1]
        g0 = graph.subgraph(part0).copy()
        g1 = graph.subgraph(part1).copy()
    else:
        part0 = [v for v, p in enumerate(parts) if p == 0]
        part1 = [v for v, p in enumerate(parts) if p == 1]
        g0 = {v: [w for w in graph[v] if w in part0] for v in part0}
        g1 = {v: [w for w in graph[v] if w in part1] for v in part1}

    return recursivecuts(g0, depth - 1) + recursivecuts(g1, depth - 1)

