"""Port of `PartitionILP.jl`.

The actual Julia code formulates an integer linear programme to obtain a
balanced partition.  In this lightweight port we simply rely on the METIS based
partitioner which gives a reasonable approximation for small graphs."""

from typing import List


def partition_ilp(hypergraph, nparts: int = 2) -> List[int]:
    from .pyspecpart import metis_partition

    G = hypergraph.to_graph()
    parts, _ = metis_partition(G, nparts)
    return parts

