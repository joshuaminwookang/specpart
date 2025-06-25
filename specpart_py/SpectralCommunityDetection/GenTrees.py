"""Generate a spanning tree of a graph."""

from typing import Any


def gentrees(graph: Any, root: int = 0) -> Any:
    if hasattr(graph, "edges"):
        import networkx as nx  # type: ignore

        tree = nx.bfs_tree(graph, root)
        return tree

    # fall back to adjacency dict
    visited = {root}
    edges = []
    from collections import deque

    dq = deque([root])
    while dq:
        u = dq.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                edges.append((u, v))
                dq.append(v)
    return edges

