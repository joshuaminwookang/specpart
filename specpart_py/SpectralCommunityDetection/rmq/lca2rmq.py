"""Convert an LCA problem on a tree to RMQ over an Euler tour."""

from typing import Any, Tuple, Dict, List


def lca2rmq(tree: Any, root: int = 0) -> Tuple[List[int], Dict[int, int]]:
    from .EulerTour import eulertour

    tour = eulertour(tree, root)
    first = {}
    for idx, v in enumerate(tour):
        first.setdefault(v, idx)
    return tour, first

