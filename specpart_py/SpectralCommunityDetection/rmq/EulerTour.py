"""Return a DFS Euler tour of a tree represented as adjacency dict."""

from typing import Any, List


def eulertour(tree: Any, root: int = 0) -> List[int]:
    tour = []

    def dfs(v, parent):
        tour.append(v)
        for w in tree[v] if isinstance(tree, dict) else tree.neighbors(v):
            if w != parent:
                dfs(w, v)
                tour.append(v)

    dfs(root, -1)
    return tour

