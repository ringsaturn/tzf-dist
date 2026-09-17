# Build Statistics

**Version:** 2026d
**Build date:** 2026-09-17T01:04:29Z

## Output Files

| File | Size | MD5 |
|------|------|-----|
| `lite.tzb` | 4.0 MB | `0dd1122453ef6c5b65f75af8e79f1836` |
| `lite.tzm` | 9.7 MB | `504fb56b9e88f0fb83578c8976ebc5b9` |
| `full.tzb` | 14.6 MB | `ec2f6ca6d4fb19d1029d582a1945d290` |

## Pipeline: `full.tzb` (dedup + compress on full precision)

### `deduplicatetzpb`

```
go: downloading github.com/tidwall/rtree v1.11.1
go: downloading github.com/ringsaturn/orb v0.15.0
go: downloading github.com/tidwall/geoindex v1.7.0
input:  timezones=444 polygons=1355 holes=791 points=8254651 bytes=121755885
output: shared_edges=3589 shared_points=4212403 inline_segs=183844 edge_ref_segs=5696 bytes=74555546
reduction: bytes=38.77%
dedup_rate: 3.01% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=74555546
output: bytes=26057835
reduction: bytes=65.05%
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
dataset_before: timezones=444 polygons=1355 holes=791 points=8254651 bytes=121755878
dataset_after:  timezones=444 polygons=1355 holes=791 points=1120947 bytes=16545738
dataset_reduction: points=86.42% bytes=86.41%
topology_rings: total=2146 no_fixed=1549 one_fixed=43 multi_fixed=550 fallback=62 hole_escape=0 resimplified=32
topology_points: input=8251080 snapped_inserted=98 fallback_points=6333 fixed_vertices=185643
topology_segments: total=187190 shared=4238(2.26%) skipped_short=182799(97.65%) skipped_small=125(0.07%) cache_hits=2111 cache_misses=2127 cache_hit_rate=49.81%
topology_segment_points: input=8438258 output=1300398 reduction=84.59%
topology_segment_length_buckets: le10=183233 le25=344 le50=345 le100=454 gt100=2814
```

### `deduplicatetzpb`

```
input:  timezones=444 polygons=1355 holes=791 points=1120947 bytes=16545745
output: shared_edges=2862 shared_points=467365 inline_segs=183794 edge_ref_segs=5646 bytes=18799751
reduction: bytes=-13.62%
dedup_rate: 2.98% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=18799751
output: bytes=13961519
reduction: bytes=25.74%
```

### `preindextzpb`

```
go: downloading golang.org/x/sync v0.22.0
input:  timezones=444 bytes=16545745
params: idxZoom=13 aggZoom=3 maxZoomLevelToKeep=10 layerDrop=2
output: total_keys=87736 bytes=2089619
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

