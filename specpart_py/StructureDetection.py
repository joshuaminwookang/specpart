"""Port of `StructureDetection.jl`."""
from typing import List


def structure_detection(h_c, incidence_struct, ubfac: int, eigs: int, community_opts: int = 1) -> List[int]:
    """Very small wrapper for community detection."""
    if community_opts == 1:
        from .pyspecpart import spectral_partition
        G = h_c.HG.to_graph()
        parts, _ = spectral_partition(G, 2)
        return parts
    return [0] * h_c.HG.num_vertices
