"""Construct a simple graph from a hypergraph for METIS."""


def buildmetisgraph(hypergraph):
    """Return the clique expansion of ``hypergraph`` as a NetworkX graph."""

    return hypergraph.to_graph()

