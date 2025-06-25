"""Simple range-min query helper."""

from typing import List


def queries(arr: List[int], l: int, r: int) -> int:
    return min(arr[l:r + 1])

