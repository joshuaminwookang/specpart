"""Port of `SpectralRefinement.jl` (simplified)."""

from typing import List


def spectral_refinement(hypergraph, parts: List[int]) -> List[int]:
    """Refine ``parts`` using one more spectral partition step."""

    from .pyspecpart import spectral_partition

    G = hypergraph.to_graph()
    new_parts, _ = spectral_partition(G, len(set(parts)))
    return new_parts

