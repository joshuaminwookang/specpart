"""Refine a partition using the simple FM heuristic."""

from typing import List


def exactrefine(hypergraph, parts: List[int]) -> List[int]:
    from ..FM import fm

    return fm(hypergraph, parts)

