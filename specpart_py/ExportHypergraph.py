"""Port of `ExportHypergraph.jl`."""
from typing import List


def export_hypergraph(hypergraph, fname: str, fixed_vtxs: List[int], idx_flag: int = 1, wt_flag: int = 0) -> None:
    """Write hypergraph in hMetis format."""
    with open(fname, "w") as f:
        f.write(f"{len(hypergraph.hyperedges)} {hypergraph.num_vertices} 11\n")
        for i, hedge in enumerate(hypergraph.hyperedges):
            verts = [v + 1 if idx_flag == 1 else v for v in hedge]
            f.write(str(hypergraph.hyperedge_weights[i]))
            for v in verts:
                f.write(f" {v}")
            f.write("\n")
        for w in hypergraph.vertex_weights:
            w_out = w + 1 if wt_flag else w
            f.write(f"{w_out}\n")

    if max(fixed_vtxs) > -1:
        with open(fname + ".fixed", "w") as f:
            for v in fixed_vtxs:
                f.write(f"{v}\n")
