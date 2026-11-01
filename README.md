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

The container format (format 1.1) is documented at
<https://project-tzf.ringsaturn.me/docs/reference/embedded-binary-format/>.

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

All three files are embedded, so a tagged version pulls ~19 MB (deflated).
Tags point at `data` branch commits; `main` only has placeholders.

```console
go get github.com/ringsaturn/tzf-dist@v0.0.2026-c-fix1
```

```go
import tzfdist "github.com/ringsaturn/tzf-dist"

// tzfdist.LiteTZB — lite .tzb (backs tzf/v2 NewEmbeddedFinder)
// tzfdist.LiteTZM — lite .tzm (backs tzf/v2 NewDefaultFinder)
// tzfdist.FullTZB — full .tzb (backs tzf/v2 NewFullFinder)
```

Most users want [`tzf`](https://github.com/ringsaturn/tzf) instead — it
depends on this module and exposes the finders directly.

## Usage (Rust crate)

The crates.io package carries `lite.tzb` only (~2.5 MB packaged); `full.tzb`
and `lite.tzm` are excluded to stay under the crates.io size limit.

```toml
[dependencies]
tzf-dist = "0.0.2026-c-fix1" # prerelease versions must be written in full
```

```rust
let data = tzf_dist::load_lite_tzb();
```

Full precision needs the `full` feature over a **git** dependency — the
feature does not compile from the crates.io package, whose `include` list
omits both `src/full.rs` and `full.tzb`.

```toml
[dependencies]
tzf-dist = { git = "https://github.com/ringsaturn/tzf-dist", tag = "...", features = ["full"], default-features = false }
```

```rust
let data = tzf_dist::load_full_tzb();
```

The `.tzm` memory image is Go-only: tzf-rs consumes the `.tzb` profile
exclusively (see the tzf-rs v2 port record in the tzf RFCs), so the Rust
crate exposes no `tzm` feature.

## Releases

Versions are `v0.0.{year}-{letter}` derived from the upstream
[timezone-boundary-builder](https://github.com/evansiroky/timezone-boundary-builder)
tag, plus an optional suffix (`-fix1`, `-tzb1`) for a rebuild of the same
upstream version. Everything after the `-` is a semver **prerelease**
identifier and is compared as ASCII text, so a new suffix must sort after
the previous one (`-tzb1` > `-fix1`).

`build.yml` (manual dispatch) regenerates the data, verifies it with tzf's
`embedcompare` gate, and force-pushes the orphan `data` branch; a tag on that
commit plus `release.yml` uploads the assets and publishes the crate.
`release.yml` takes a `dry_run` input — use it first: tags are immutable on
both the Go module proxy and crates.io.

Binary files are attached to each GitHub Release as assets, alongside
`STATS.md`, `BORDER_CHANGE.md` and `checksums.md5`.

## License

Code is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Data is licensed under ODbL. See [LICENSE_DATA](LICENSE_DATA) for details. Same
with the
[timezone-boundary-builder](https://github.com/evansiroky/timezone-boundary-builder).
