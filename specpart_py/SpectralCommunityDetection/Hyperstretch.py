"""Compute a very rough 'stretch' of a hypergraph."""

from typing import List


def hyperstretch(hypergraph, embedding: List[float]) -> float:
    total = 0.0
    for hedge in hypergraph.hyperedges:
        vals = [embedding[v] for v in hedge]
        total += max(vals) - min(vals)
    return total / max(1, len(hypergraph.hyperedges))

