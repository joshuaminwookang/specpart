"""Utility to generate a BFS sweep ordering of a tree."""

from typing import Any, List


def treesweeputilities(tree: Any, root: int = 0) -> List[int]:
    order = []
    from collections import deque

    dq = deque([root])
    visited = {root}
    while dq:
        v = dq.popleft()
        order.append(v)
        for w in tree[v] if isinstance(tree, dict) else tree.neighbors(v):
            if w not in visited:
                visited.add(w)
                dq.append(w)
    return order

