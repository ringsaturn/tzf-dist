# Build Statistics

**Version:** 2026f
**Build date:** 2026-11-01T04:11:08Z

## Output Files

| File | Size | MD5 |
|------|------|-----|
| `lite.tzb` | 3.9 MB | `39e35c15c1f1f01f747bb38b226c401c` |
| `lite.tzm` | 9.8 MB | `6ee2e1557af17a56f334bcc7ed75691b` |
| `full.tzb` | 14.7 MB | `cee514b502c2855a0288c48cf2c1b5c1` |

## Pipeline: `full.tzb` (dedup + compress on full precision)

### `deduplicatetzpb`

```
go: downloading github.com/ringsaturn/orb v0.15.0
go: downloading github.com/tidwall/rtree v1.11.1
go: downloading github.com/tidwall/geoindex v1.7.0
input:  timezones=444 polygons=1356 holes=792 points=8296476 bytes=122372575
output: shared_edges=3587 shared_points=4232886 inline_segs=184899 edge_ref_segs=5696 bytes=74937557
reduction: bytes=38.76%
dedup_rate: 2.99% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=74937557
output: bytes=26183970
reduction: bytes=65.06%
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
dataset_before: timezones=444 polygons=1356 holes=792 points=8296476 bytes=122372568
dataset_after:  timezones=444 polygons=1356 holes=792 points=1131787 bytes=16705598
dataset_reduction: points=86.36% bytes=86.35%
topology_rings: total=2148 no_fixed=1521 one_fixed=8 multi_fixed=615 fallback=66 hole_escape=0 resimplified=39
topology_points: input=8292880 snapped_inserted=97 fallback_points=10083 fixed_vertices=188595
topology_segments: total=190112 shared=5455(2.87%) skipped_short=184853(97.23%) skipped_small=209(0.11%) cache_hits=2708 cache_misses=2747 cache_hit_rate=49.64%
topology_segment_points: input=8482980 output=1310055 reduction=84.56%
topology_segment_length_buckets: le10=185474 le25=434 le50=457 le100=573 gt100=3174
```

### `deduplicatetzpb`

```
input:  timezones=444 polygons=1356 holes=792 points=1131787 bytes=16705605
output: shared_edges=2533 shared_points=477238 inline_segs=184137 edge_ref_segs=4968 bytes=18852005
reduction: bytes=-12.85%
dedup_rate: 2.63% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=18852005
output: bytes=13946451
reduction: bytes=26.02%
```

### `preindextzpb`

```
go: downloading golang.org/x/sync v0.23.0
input:  timezones=444 bytes=16705605
params: idxZoom=13 aggZoom=3 maxZoomLevelToKeep=10 layerDrop=2
output: total_keys=87665 bytes=2087591
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

