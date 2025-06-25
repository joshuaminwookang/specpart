import argparse
import os
from glob import glob

from specpart_py.pyspecpart import partition_hgr, spectral_partition_hgr


def run_on_file(path: str, method: str = "metis"):
    if method == "metis":
        parts = partition_hgr(path)
    else:
        parts = spectral_partition_hgr(path)
    print(f"{os.path.basename(path)}: {parts[:10]}{'...' if len(parts) > 10 else ''}")


def gather_files(base_dir: str, limit: int = 0):
    patterns = [
        os.path.join(base_dir, "ISPD_benchmark", "*.hgr"),
        os.path.join(base_dir, "ISPD_weight_benchmark", "*.hgr"),
        os.path.join(base_dir, "Titan23_benchmark", "*.hgr"),
    ]
    files = []
    for pattern in patterns:
        files.extend(sorted(glob(pattern)))
        if limit and len(files) >= limit:
            break
    return files[:limit] if limit else files


def main():
    parser = argparse.ArgumentParser(description="Run partitions on benchmark graphs")
    parser.add_argument("--bench-dir", default="benchmark", help="Benchmark directory")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of graphs")
    parser.add_argument("--method", choices=["metis", "spectral"], default="metis")
    args = parser.parse_args()

    files = gather_files(args.bench_dir, args.limit)
    for path in files:
        run_on_file(path, args.method)


if __name__ == "__main__":
    main()
