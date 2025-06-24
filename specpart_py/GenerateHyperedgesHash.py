"""Utilities mirroring `GenerateHyperedgesHash.jl`."""
from typing import Dict, List


def generate_hyperedges_hash(hypergraph) -> Dict[int, int]:
    """Create a simple hash for each hyperedge based on its vertices."""
    hmap: Dict[int, int] = {}
    for idx, hedge in enumerate(hypergraph.hyperedges):
        hmap[idx] = sum(v * v for v in hedge)
    return hmap
