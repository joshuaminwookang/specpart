"""Simplified version of Prim's algorithm using NetworkX."""

from typing import Any


def modified_prims(graph: Any, start: int = 0) -> Any:
    if hasattr(graph, "edges"):
        import networkx as nx  # type: ignore

        tree = nx.minimum_spanning_tree(graph)
        return tree

    from .GenTrees import gentrees
    return gentrees(graph, start)

