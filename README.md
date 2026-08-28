# tzf-dist

Binary data distribution for [tzf](https://github.com/ringsaturn/tzf) and
[tzf-rs](https://github.com/ringsaturn/tzf-rs).

If you have any questions or suggestions, please open an issue in the
[upstream tzf repository](https://github.com/ringsaturn/tzf).

## Files

| File       | Format                    | Size   | Description                                                        |
| ---------- | ------------------------- | ------ | ------------------------------------------------------------------ |
| `lite.tzb` | TZF embedded binary (E)   | ~4MB   | Lite: topology-aware simplify + dedup + compression, FUZZY preindex included |
| `lite.tzm` | TZF embedded binary (M)   | ~10MB  | Memory image of `lite.tzb`: the file is the query-time structure   |
| `full.tzb` | TZF embedded binary (E)   | ~14MB  | Full precision: dedup + compression, FUZZY preindex included       |

All three files carry the same `data_version`. `full.tzm` is never
distributed — derive it locally with tzf's `tzb2tzm` when needed.

The container format is specified in the tzf repository
(`rfc/tzf/2026-07-19-tzf-for-embedded-bin.spec-v1.md`, format 1.1).

Releases up to `v0.0.2026-c-fix1` distributed the retired protobuf artifact
set (`CompressedTopoTimezones` / `PreindexTimezones`); those tags remain
available for the frozen tzf v1 line and pre-`.tzb` tzf-rs versions.

## Branch structure

- **`main`** — source code, workflows, and `embed.go` template; never tagged
- **`data`** — latest generated binaries as an orphan commit (force-pushed on
  each update); the tip commit is what gets tagged for releases

Historical data is accessible via tags — each tag points to a single orphan
commit on `data` that contains the binary files for that
timezone-boundary-builder version.

Each `data` commit also contains `STATS.md` for compression statistics and
`BORDER_CHANGE.md` for simplification accuracy statistics. Both reports are
included in the corresponding GitHub Release notes.

## Usage (Go module)

Import a tagged version (tags point to `data` branch commits containing the
embedded files):

```go
import tzfdist "github.com/ringsaturn/tzf-dist"

// tzfdist.LiteTZB — lite .tzb (backs tzf/v2 NewEmbeddedFinder)
// tzfdist.LiteTZM — lite .tzm (backs tzf/v2 NewDefaultFinder)
// tzfdist.FullTZB — full .tzb (backs tzf/v2 NewFullFinder)
```

## Usage (Rust crate)

```toml
[dependencies]
tzf-dist = "..."
```

```rust
let data = tzf_dist::load_lite_tzb();
```

If you need full data precision or the `.tzm` memory image, use the `full` /
`tzm` feature flags with a git based dependency (those files are not
available on crates.io due to size constraints):

```toml
[dependencies]
tzf-dist = { git = "https://github.com/ringsaturn/tzf-dist", tag = "...", features = ["full"], default-features = false}
```

## Releases

Binary files are attached to each GitHub Release as assets, built from the
corresponding
[timezone-boundary-builder](https://github.com/evansiroky/timezone-boundary-builder)
release.

Tags are created manually from the `data` branch tip after automated data
generation. Creating a GitHub Release from a tag triggers asset upload via the
release workflow.

## License

Code is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Data is licensed under ODbL. See [DATA_LICENSE](DATA_LICENSE) for details. Same
with the
[timezone-boundary-builder](https://github.com/evansiroky/timezone-boundary-builder).
