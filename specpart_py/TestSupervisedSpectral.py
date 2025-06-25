"""Small routine emulating the Julia tests for supervised spectral clustering."""

from typing import List, Tuple


def test_supervised_spectral(hypergraph, labels: List[int]) -> Tuple[List[int], int]:
    """Run spectral clustering and report the number of mistakes."""

    from .pyspecpart import spectral_partition

    G = hypergraph.to_graph()
    parts, _ = spectral_partition(G, len(set(labels)))
    mistakes = sum(int(p != l) for p, l in zip(parts, labels))
    return parts, mistakes

