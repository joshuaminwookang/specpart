"""Simple wrapper performing spectral clustering on a graph."""

from typing import List


def clustering(graph, k: int = 2) -> List[int]:
    from ..pyspecpart import spectral_partition

    parts, _ = spectral_partition(graph, k)
    return parts

