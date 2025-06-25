"""Port of `FM.jl`.

This provides a very small and inefficient version of the classical
Fiduccia--Mattheyses refinement algorithm.  The implementation iteratively
checks whether moving a single vertex to the opposite side decreases the cut.
It is intended only for small toy examples used in the tests."""

from typing import List


def _cut(hg, parts: List[int]) -> int:
    cut = 0
    for hedge, w in zip(hg.hyperedges, hg.hyperedge_weights):
        if len({parts[v] for v in hedge}) > 1:
            cut += w
    return cut


def fm(hg, parts: List[int]) -> List[int]:
    """Return a refined partition vector."""

    best = parts[:]
    best_cut = _cut(hg, best)
    improved = True
    while improved:
        improved = False
        for v in range(hg.num_vertices):
            trial = best[:]
            trial[v] = 1 - trial[v]
            c = _cut(hg, trial)
            if c < best_cut:
                best_cut = c
                best = trial
                improved = True
    return best

