"""Generate trivial hints for community seeds."""

from typing import List


def generatehints(parts: List[int]) -> List[int]:
    seen = set()
    hints = []
    for idx, p in enumerate(parts):
        if p not in seen:
            hints.append(idx)
            seen.add(p)
    return hints

