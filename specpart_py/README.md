# PySpecPart

This is a minimal Python re-implementation of some features of the original
SpecPart library written in Julia.  The implementation relies on
[NetworkX](https://networkx.org/) for graph manipulation and
[PyMetis](https://pypi.org/project/pymetis/) for graph partitioning.  A simple
spectral partitioner implemented with NumPy is also provided.

The module provides utilities to load hypergraphs stored in hMetis `.hgr`
format, convert them to graphs via clique expansion and partition them using
either PyMetis or a spectral method.

## Usage

```python
from specpart_py.pyspecpart import partition_hgr, spectral_partition_hgr

# METIS based partition
parts = partition_hgr("path/to/hypergraph.hgr", nparts=2)

# Spectral bipartition
spectral_parts = spectral_partition_hgr("path/to/hypergraph.hgr")
print(parts, spectral_parts)
```

The returned list contains the part id for each vertex.  The optional
`nparts` argument controls the number of desired partitions (default is `2`).

## Requirements

* Python 3.8+
* `networkx`, `numpy`, and `pymetis` installed. These can be installed via pip:

```bash
pip install networkx numpy pymetis
```

Note that these packages are not included in this repository.
