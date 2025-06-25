"""Light-weight helpers for partition structures."""

from typing import Dict, List


def partition_structures(parts: List[int]) -> Dict[int, List[int]]:
    """Return a dictionary mapping part id to list of vertices."""

    res: Dict[int, List[int]] = {}
    for idx, p in enumerate(parts):
        res.setdefault(p, []).append(idx)
    return res

