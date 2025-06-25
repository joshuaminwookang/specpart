"""Solve a range minimum query using a prefix-min table."""

from typing import List


def rmq_solve(prefix: List[int], arr: List[int], l: int, r: int) -> int:
    if l == 0:
        return prefix[r]
    return min(prefix[r], min(arr[l:r + 1]))

