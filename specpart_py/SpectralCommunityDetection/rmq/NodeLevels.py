"""Compute the level (depth) of each node in a tree."""

from typing import Any, Dict


def nodelevels(tree: Any, root: int = 0) -> Dict[int, int]:
    from collections import deque

    level = {root: 0}
    dq = deque([root])
    while dq:
        v = dq.popleft()
        for w in tree[v] if isinstance(tree, dict) else tree.neighbors(v):
            if w not in level:
                level[w] = level[v] + 1
                dq.append(w)
    return level

