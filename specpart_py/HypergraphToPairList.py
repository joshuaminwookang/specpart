"""Port of `HypergraphToPairList.jl`."""
from typing import List, Tuple


def generate_hypergraph_pair_list(hypergraph) -> List[Tuple[int, int]]:
    """Return (start,end) indices for each hyperedge in flattened array."""
    pair_list = []
    start = 0
    for hedge in hypergraph.hyperedges:
        pair_list.append((start, start + len(hedge) - 1))
        start += len(hedge)
    return pair_list
