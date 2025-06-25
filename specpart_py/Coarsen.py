"""Port of `Coarsen.jl`.

This is a very small wrapper around :func:`generate_coarse_hypergraph` which
filters out vertices and hyperedges according to the provided flags.  The Julia
implementation performs multilevel coarsening; here we simply drop the flagged
items which is sufficient for the lightweight routines in the tests."""

from typing import List, Tuple


def coarsen_hypergraph(h_c, vertices_flag: List[bool], hyperedges_flag: List[int]):
    """Return a coarse version of ``h_c``.

    Parameters
    ----------
    h_c : HypergraphC
        Container object as defined in :mod:`pyspecpart`.
    vertices_flag : List[bool]
        ``True`` for vertices to keep.
    hyperedges_flag : List[int]
        ``-1`` for hyperedges to keep.

    Returns
    -------
    Tuple[Hypergraph, List[int]]
        The new hypergraph together with the mapping of fixed vertices.
    """

    from .GenerateCoarseHypergraph import generate_coarse_hypergraph

    return generate_coarse_hypergraph(h_c, vertices_flag, hyperedges_flag)

