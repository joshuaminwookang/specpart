"""Combine multiple partition vectors by majority vote."""

from typing import Iterable, List


def combinepartitions(partitions: Iterable[List[int]]) -> List[int]:
    parts = list(partitions)
    if not parts:
        return []
    n = len(parts[0])
    result = []
    for i in range(n):
        votes = {}
        for p in parts:
            votes[p[i]] = votes.get(p[i], 0) + 1
        result.append(max(votes, key=votes.get))
    return result

