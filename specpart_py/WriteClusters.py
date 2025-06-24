"""Port of `WriteClusters.jl`."""
from typing import List


def write_clusters(community: List[int], fname: str = "clusters.dat") -> None:
    """Write community assignments to a file."""
    with open(fname, "w") as f:
        for idx, c in enumerate(community, start=1):
            f.write(f"{idx},{c}\n")
