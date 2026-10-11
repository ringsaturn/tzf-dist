# Build Statistics

**Version:** 2026e
**Build date:** 2026-10-11T05:14:15Z

## Output Files

| File | Size | MD5 |
|------|------|-----|
| `lite.tzb` | 3.9 MB | `350b5048329073895ace754da9c91117` |
| `lite.tzm` | 9.8 MB | `3c5d116cdef33c95ab1fdce00c62c79a` |
| `full.tzb` | 14.7 MB | `8dfb3a2328883c8e8d5dc1c4474bee54` |

## Pipeline: `full.tzb` (dedup + compress on full precision)

### `deduplicatetzpb`

```
go: downloading github.com/ringsaturn/orb v0.15.0
go: downloading github.com/tidwall/rtree v1.11.1
go: downloading github.com/tidwall/geoindex v1.7.0
input:  timezones=444 polygons=1358 holes=795 points=8285828 bytes=122215636
output: shared_edges=3596 shared_points=4228319 inline_segs=184121 edge_ref_segs=5708 bytes=74809934
reduction: bytes=38.79%
dedup_rate: 3.01% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=74809934
output: bytes=26125173
reduction: bytes=65.08%
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
dataset_before: timezones=444 polygons=1358 holes=795 points=8285828 bytes=122215629
dataset_after:  timezones=444 polygons=1358 holes=795 points=1131106 bytes=16695539
dataset_reduction: points=86.35% bytes=86.34%
topology_rings: total=2153 no_fixed=1526 one_fixed=8 multi_fixed=615 fallback=68 hole_escape=0 resimplified=40
topology_points: input=8282223 snapped_inserted=97 fallback_points=10107 fixed_vertices=187816
topology_segments: total=189338 shared=5463(2.89%) skipped_short=184074(97.22%) skipped_small=210(0.11%) cache_hits=2711 cache_misses=2752 cache_hit_rate=49.62%
topology_segment_points: input=8471549 output=1308573 reduction=84.55%
topology_segment_length_buckets: le10=184697 le25=438 le50=456 le100=573 gt100=3174
```

### `deduplicatetzpb`

```
input:  timezones=444 polygons=1358 holes=795 points=1131106 bytes=16695546
output: shared_edges=2539 shared_points=477323 inline_segs=183355 edge_ref_segs=4976 bytes=18804257
reduction: bytes=-12.63%
dedup_rate: 2.64% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=18804257
output: bytes=13903158
reduction: bytes=26.06%
```

### `preindextzpb`

```
go: downloading golang.org/x/sync v0.22.0
input:  timezones=444 bytes=16695546
params: idxZoom=13 aggZoom=3 maxZoomLevelToKeep=10 layerDrop=2
output: total_keys=87653 bytes=2087310
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

