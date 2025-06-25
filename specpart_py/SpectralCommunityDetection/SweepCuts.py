"""Evaluate all sweep cuts of a vector."""

from typing import Iterable, List, Any


def sweepcuts(graph: Any, ordering: Iterable[int]) -> List[int]:
    from .CutProfile import cutprofile

    return cutprofile(graph, ordering)

