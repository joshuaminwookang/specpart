"""Compute the best sweep cut of an ordering."""

from typing import Iterable, Any


def analyzespectralcuts(graph: Any, ordering: Iterable[int]) -> int:
    from .CutProfile import cutprofile

    cuts = cutprofile(graph, ordering)
    return min(cuts) if cuts else 0

