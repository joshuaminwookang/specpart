"""Thin wrapper over :func:`~pyspecpart.spectral_partition`."""

from typing import Any, List


def spectralpartitioning(graph: Any, k: int = 2) -> List[int]:
    from ..pyspecpart import spectral_partition

    parts, _ = spectral_partition(graph, k)
    return parts

