"""Port of `InitialPartitions.jl`."""
from typing import List, Tuple
import random


def generate_random_initial_partitions(vertex_weights: List[int], max_capacity: int, min_capacity: int) -> Tuple[List[int], List[int]]:
    """Create a random feasible bipartition respecting capacities."""
    n = len(vertex_weights)
    vertices = list(range(n))
    random.shuffle(vertices)
    part_vector = [-1] * n
    part_area = [0, 0]
    for v in vertices:
        poss = part_area[0] + vertex_weights[v]
        if poss < max_capacity:
            part_vector[v] = 0
            part_area[0] = poss
        else:
            part_vector[v] = 1
            part_area[1] += vertex_weights[v]
    return part_vector, part_area
