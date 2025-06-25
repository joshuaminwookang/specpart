"""Detect communities using spectral partitioning."""

from typing import Any, List


def spectralcommunities(graph: Any, k: int = 2) -> List[int]:
    from ..pyspecpart import spectral_partition

    parts, _ = spectral_partition(graph, k)
    return parts

