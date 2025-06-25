"""Find all triangles in a graph."""

from typing import Any, List, Tuple


def dcliques(graph: Any) -> List[Tuple[int, int, int]]:
    triangles = []
    nodes = list(graph.nodes()) if hasattr(graph, "nodes") else list(graph.keys())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                u, v, w = nodes[i], nodes[j], nodes[k]
                if hasattr(graph, "has_edge"):
                    cond = graph.has_edge(u, v) and graph.has_edge(v, w) and graph.has_edge(u, w)
                else:
                    cond = v in graph[u] and w in graph[v] and w in graph[u]
                if cond:
                    triangles.append((u, v, w))
    return triangles

