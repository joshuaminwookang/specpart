"""Compute a simple cut profile of a sweep ordering."""

from typing import Iterable, List


def cutprofile(graph, ordering: Iterable[int]) -> List[int]:
    """Return the cut size after each vertex in ``ordering`` is added."""

    order = list(ordering)
    part = [1] * len(order)
    cuts = []
    curr = 0
    for idx in order:
        part[idx] = 0
        # compute cut
        cut = 0
        for u, nbrs in graph.items() if isinstance(graph, dict) else graph.adj.items():
            for v in nbrs:
                if u < v and part[u] != part[v]:
                    cut += 1
        cuts.append(cut)
    return cuts

