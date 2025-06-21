import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import pytest

from specpart_py import spectral_partition_hgr


def test_simple_hgr_partition():
    hgr_path = os.path.join(os.path.dirname(__file__), 'data', 'simple.hgr')
    parts = spectral_partition_hgr(hgr_path)
    assert parts == [0, 0, 1, 1]
