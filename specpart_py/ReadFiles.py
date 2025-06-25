"""Utility loader matching the Julia `ReadFiles.jl` interface."""

from typing import Any


def read_files(path: str) -> Any:
    """Read a hypergraph from ``path`` using :class:`Hypergraph`."""

    from .pyspecpart import Hypergraph

    if not path.endswith(".hgr"):
        raise ValueError("Only .hgr format supported in this simplified port")

    return Hypergraph.from_hgr(path)

