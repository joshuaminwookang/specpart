"""Compute a bipartition of a tree by alternating levels."""

from typing import Any, List


def treebipartition(tree: Any, root: int = 0) -> List[int]:
    parts = {}
    from collections import deque

    dq = deque([(root, 0)])
    parts[root] = 0
    while dq:
        v, p = dq.popleft()
        for w in tree[v] if isinstance(tree, dict) else tree.neighbors(v):
            if w not in parts:
                parts[w] = 1 - p
                dq.append((w, 1 - p))
    return [parts[i] for i in sorted(parts)]

