# tzf-dist

Binary data distribution for [tzf](https://github.com/ringsaturn/tzf) — timezone lookup data in next-generation formats.

## Files

| File | Format | Size | Description |
|------|--------|------|-------------|
| `combined-with-oceans.compress.topo.bin` | `CompressedTopoTimezones` | ~17MB | Full precision: shared-edge dedup + polyline compression |
| `combined-with-oceans.topology.compress.topo.bin` | `CompressedTopoTimezones` | ~5.4MB | Lite: topology-aware simplify + shared-edge dedup + polyline compression |
| `combined-with-oceans.reduce.preindex.bin` | `PreindexTimezones` | ~2MB | Tile pre-index for FuzzyFinder |

## Branch structure

- **`main`** — source code, workflows, and `embed.go` template; never tagged
- **`data`** — latest generated binaries as an orphan commit (force-pushed on each update); the tip commit is what gets tagged for releases

Historical data is accessible via tags — each tag points to a single orphan commit on `data` that contains the binary files for that timezone-boundary-builder version.

## Usage (Go module)

Import a tagged version (tags point to `data` branch commits containing the embedded files):

```go
import tzfdist "github.com/ringsaturn/tzf-dist"

// tzfdist.CompressTopoData        — full precision CompressedTopoTimezones
// tzfdist.TopologyCompressTopoData — lite CompressedTopoTimezones
// tzfdist.PreindexData             — tile pre-index
```

## Releases

Binary files are attached to each GitHub Release as assets, built from the corresponding [timezone-boundary-builder](https://github.com/evansiroky/timezone-boundary-builder) release.

Tags are created manually from the `data` branch tip after automated data generation. Creating a GitHub Release from a tag triggers asset upload via the release workflow.
