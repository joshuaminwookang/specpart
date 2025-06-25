"""Reconstruct a tree using a simple MST approach."""

from typing import Any


def iterativemstreconstruction(graph: Any) -> Any:
    if hasattr(graph, "edges"):
        import networkx as nx  # type: ignore

        return nx.minimum_spanning_tree(graph)

    # approximate with BFS tree
    from .GenTrees import gentrees
    return gentrees(graph)

