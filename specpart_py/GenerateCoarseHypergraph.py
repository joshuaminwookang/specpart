"""Port of `GenerateCoarseHypergraph.jl`."""
from typing import List, Tuple


def generate_coarse_hypergraph(h_c, vertices_flag: List[bool], hyperedges_flag: List[int]) -> Tuple["Hypergraph", List[int]]:
    """Construct a coarse hypergraph by removing flagged vertices/edges."""
    from .pyspecpart import Hypergraph  # local import to avoid circular deps
    vertex_map = {}
    new_vertices = []
    fixed_cc = []
    for idx in range(h_c.HG.num_vertices):
        if (h_c.fixed_vertex_flag and h_c.fixed_part[idx] > -1) or not vertices_flag[idx]:
            vertex_map[idx] = len(new_vertices)
            new_vertices.append(h_c.HG.vertex_weights[idx])
            fixed_cc.append(h_c.fixed_part[idx])
    hyperedges_cc = []
    edge_wts = []
    for idx, hedge in enumerate(h_c.HG.hyperedges):
        if hyperedges_flag[idx] == -1:
            new_edge = [vertex_map[v] for v in hedge if v in vertex_map]
            if new_edge:
                hyperedges_cc.append(new_edge)
                edge_wts.append(h_c.HG.hyperedge_weights[idx])

    cc_hg = Hypergraph(len(new_vertices), hyperedges_cc, new_vertices, edge_wts)
    return cc_hg, fixed_cc
