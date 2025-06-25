"""Simplified driver for the CMG algorithm."""

from typing import Any


def cmgalg(graph: Any) -> Any:
    from .CombinatorialMultigrid import combinatorialmultigrid

    return combinatorialmultigrid(graph)

