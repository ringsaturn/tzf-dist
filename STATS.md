# Build Statistics

**Version:** 2026c-tzb2
**Build date:** 2026-09-14T00:28:25Z

## Output Files

| File | Size | MD5 |
|------|------|-----|
| `lite.tzb` | 4.0 MB | `5bdae4f6b1038514be6a3ef82efd52b6` |
| `lite.tzm` | 9.7 MB | `790a6b65c42a6752302e0dd20dea6c79` |
| `full.tzb` | 14.6 MB | `3bdab68ea8e0ac8c87a373c575423147` |

## Pipeline: `full.tzb` (dedup + compress on full precision)

### `deduplicatetzpb`

```
go: downloading github.com/ringsaturn/orb v0.15.0
go: downloading github.com/tidwall/rtree v1.11.1
go: downloading github.com/tidwall/geoindex v1.7.0
input:  timezones=444 polygons=1322 holes=756 points=8189808 bytes=120799059
output: shared_edges=3529 shared_points=4181234 inline_segs=183854 edge_ref_segs=5620 bytes=74075538
reduction: bytes=38.68%
dedup_rate: 2.97% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=74075538
output: bytes=25960605
reduction: bytes=64.95%
```

### `topo2embed -profile e`

```
../tzf-dist/full.tzb
```

## Pipeline: `lite.tzb` (topology-aware simplify + dedup + compress + preindex)

### `reducetzpb -topology=true`

```
mode: topology
epsilon: 0.001000
dataset_before: timezones=444 polygons=1322 holes=756 points=8189808 bytes=120799052
dataset_after:  timezones=444 polygons=1322 holes=756 points=1117128 bytes=16489109
dataset_reduction: points=86.36% bytes=86.35%
topology_rings: total=2078 no_fixed=1485 one_fixed=39 multi_fixed=550 fallback=207
topology_points: input=8186335 snapped_inserted=98 fallback_points=10712 fixed_vertices=185657
topology_segments: total=187140 shared=4170(2.23%) skipped_short=182817(97.69%) cache_hits=2077 cache_misses=2093 cache_hit_rate=49.81%
topology_segment_points: input=8373463 output=1292118 reduction=84.57%
topology_segment_length_buckets: le10=183203 le25=332 le50=342 le100=448 gt100=2815
```

### `deduplicatetzpb`

```
input:  timezones=444 polygons=1322 holes=756 points=1117128 bytes=16489116
output: shared_edges=2907 shared_points=467905 inline_segs=183838 edge_ref_segs=5592 bytes=18810713
reduction: bytes=-14.08%
dedup_rate: 2.95% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=18810713
output: bytes=13961374
reduction: bytes=25.78%
```

### `preindextzpb`

```
go: downloading golang.org/x/sync v0.22.0
input:  timezones=444 bytes=16489116
params: idxZoom=13 aggZoom=3 maxZoomLevelToKeep=10 layerDrop=2
output: total_keys=87728 bytes=2089412
```

### `topo2embed -profile e -preindex`

```
../tzf-dist/lite.tzb
```

## Pipeline: `lite.tzm` (memory-image transcode of lite.tzb)

### `tzb2tzm`

```
../tzf-dist/lite.tzm
```

