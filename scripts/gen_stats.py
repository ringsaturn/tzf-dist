#!/usr/bin/env python3
"""Generate STATS.md from pipeline stderr captures and output file checksums.

Environment variables required:
  TBB_VERSION   - timezone-boundary-builder version string (e.g. "2026a")
  BUILD_DATE    - ISO-8601 UTC build timestamp

Reads stats from /tmp/stats-*.txt written by the CI pipeline steps.
Writes STATS.md in the current directory.
"""

import hashlib
import os
import pathlib

FILES = [
    "combined-with-oceans.compress.topo.bin",
    "combined-with-oceans.topology.compress.topo.bin",
    "combined-with-oceans.reduce.preindex.bin",
]

SECTIONS = [
    (
        "## Pipeline: `compress.topo.bin` (dedup + compress on full precision)",
        [
            ("deduplicatetzpb", "/tmp/stats-dedup-full.txt"),
            ("compresstopotzpb", "/tmp/stats-compress-full.txt"),
        ],
    ),
    (
        "## Pipeline: `topology.compress.topo.bin` (topology-aware simplify + dedup + compress)",
        [
            ("reducetzpb -topology=true", "/tmp/stats-reduce-topo.txt"),
            ("deduplicatetzpb", "/tmp/stats-dedup-topo.txt"),
            ("compresstopotzpb", "/tmp/stats-compress-topo.txt"),
        ],
    ),
    (
        "## Pipeline: `reduce.preindex.bin` (classic simplify + preindex)",
        [
            ("reducetzpb -topology=false", "/tmp/stats-reduce-classic.txt"),
        ],
    ),
]


def read_stats(path):
    try:
        return pathlib.Path(path).read_text().strip()
    except FileNotFoundError:
        return "(no output)"


def fmt_size(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} GB"


def main():
    lines = [
        "# Build Statistics",
        "",
        f"**Timezone Boundary Builder version:** {os.environ['TIMEZONE_BOUNDARY_VERSION']}",
        f"**Build date:** {os.environ['BUILD_DATE']}",
        "",
        "## Output Files",
        "",
        "| File | Size | MD5 |",
        "|------|------|-----|",
    ]

    for f in FILES:
        size = fmt_size(os.path.getsize(f))
        md5 = hashlib.md5(open(f, "rb").read()).hexdigest()
        lines.append(f"| `{f}` | {size} | `{md5}` |")
    lines.append("")

    for heading, steps in SECTIONS:
        lines += [heading, ""]
        for tool, path in steps:
            lines += [
                f"### `{tool}`",
                "",
                "```",
                read_stats(path),
                "```",
                "",
            ]

    pathlib.Path("STATS.md").write_text("\n".join(lines) + "\n")
    print("STATS.md written")


if __name__ == "__main__":
    main()
