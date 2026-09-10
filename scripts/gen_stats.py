#!/usr/bin/env python3
"""Generate STATS.md from pipeline stderr captures and output file checksums.

Environment variables required:
  DIST_VERSION  - distribution version: TBB version plus optional suffix
                  (e.g. "2026c", "2026c-tzb1")
  BUILD_DATE    - ISO-8601 UTC build timestamp

Reads stats from /tmp/stats-*.txt written by the CI pipeline steps.
Writes STATS.md in the current directory.
"""

import hashlib
import os
import pathlib

FILES = [
    "lite.tzb",
    "lite.tzm",
    "full.tzb",
]

SECTIONS = [
    (
        "## Pipeline: `full.tzb` (dedup + compress on full precision)",
        [
            ("deduplicatetzpb", "/tmp/stats-dedup-full.txt"),
            ("compresstopotzpb", "/tmp/stats-compress-full.txt"),
            ("topo2embed -profile e", "/tmp/stats-embed-full.txt"),
        ],
    ),
    (
        "## Pipeline: `lite.tzb` (topology-aware simplify + dedup + compress + preindex)",
        [
            ("reducetzpb -topology=true", "/tmp/stats-reduce-topo.txt"),
            ("deduplicatetzpb", "/tmp/stats-dedup-topo.txt"),
            ("compresstopotzpb", "/tmp/stats-compress-topo.txt"),
            ("preindextzpb", "/tmp/stats-preindex.txt"),
            ("topo2embed -profile e -preindex", "/tmp/stats-embed-lite.txt"),
        ],
    ),
    (
        "## Pipeline: `lite.tzm` (memory-image transcode of lite.tzb)",
        [
            ("tzb2tzm", "/tmp/stats-tzm.txt"),
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
        f"**Version:** {os.environ['DIST_VERSION']}",
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
