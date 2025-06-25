"""Check whether two vertex sets form a biclique."""

from typing import Iterable


def dbiclique(graph, left: Iterable[int], right: Iterable[int]) -> bool:
    left = list(left)
    right = list(right)
    for u in left:
        for v in right:
            if hasattr(graph, "has_edge"):
                if not graph.has_edge(u, v):
                    return False
            else:
                if v not in graph[u]:
                    return False
    return True

