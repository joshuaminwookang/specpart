"""Return the list of hyperedges of size two."""

from typing import List


def generatetwopinhyperedges(hypergraph) -> List[List[int]]:
    return [e for e in hypergraph.hyperedges if len(e) == 2]

