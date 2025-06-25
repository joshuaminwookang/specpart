"""Return connected components of a graph."""

from typing import Any, List


def isolateislands(graph: Any) -> List[List[int]]:
    if hasattr(graph, "subgraph"):
        import networkx as nx  # type: ignore
        return [list(c) for c in nx.connected_components(graph)]

    visited = set()
    comps = []
    from collections import deque

    for v in graph:
        if v in visited:
            continue
        comp = []
        dq = deque([v])
        visited.add(v)
        while dq:
            u = dq.popleft()
            comp.append(u)
            for w in graph[u]:
                if w not in visited:
                    visited.add(w)
                    dq.append(w)
        comps.append(comp)
    return comps

