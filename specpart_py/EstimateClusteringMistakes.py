"""Port of `EstimateClusteringMistakes.jl`.

The real Julia routine estimates the number of misplaced vertices when a
partition is compared against ground truth.  For the purposes of this Python
port we simply count the mismatches between the two vectors."""

from typing import List


def estimate_clustering_mistakes(assignment: List[int], ground_truth: List[int]) -> int:
    """Return how many vertices are assigned to a different community."""

    if len(assignment) != len(ground_truth):
        raise ValueError("Vectors must have the same length")

    mistakes = sum(int(a != b) for a, b in zip(assignment, ground_truth))
    return mistakes

