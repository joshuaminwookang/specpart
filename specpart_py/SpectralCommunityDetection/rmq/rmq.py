"""Build a prefix-min table for range minimum queries."""

from typing import List


def rmq(arr: List[int]) -> List[int]:
    pref = [arr[0]]
    for v in arr[1:]:
        pref.append(min(pref[-1], v))
    return pref

