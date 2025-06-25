"""A tiny script mirroring the behaviour of the Julia `TestScript.jl`."""


def test_script():
    from .pyspecpart import Hypergraph, spectral_partition

    hg = Hypergraph(4, [[0, 1], [1, 2], [2, 3]])
    G = hg.to_graph()
    parts, cut = spectral_partition(G)
    return parts, cut

