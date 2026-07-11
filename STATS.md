# Build Statistics

**Version:** 2026c
**Build date:** 2026-07-11T11:05:05Z

## Output Files

| File | Size | MD5 |
|------|------|-----|
| `combined-with-oceans.compress.topo.bin` | 18.0 MB | `52420ba4e207b02ce2e9b29dab440006` |
| `combined-with-oceans.topology.compress.topo.bin` | 6.5 MB | `211c4cdadf92513d40bb93a93fa23a7e` |
| `combined-with-oceans.topology.preindex.bin` | 2.0 MB | `cbc59be2e054c978147219db663c1ddf` |

## Pipeline: `compress.topo.bin` (dedup + compress on full precision)

### `deduplicatetzpb`

```
input:  timezones=444 polygons=1322 holes=756 points=8189808 bytes=98293435
output: shared_edges=3529 shared_points=4181234 inline_segs=183854 edge_ref_segs=5620 bytes=55924363
reduction: bytes=43.10%
dedup_rate: 2.97% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=55924363
output: bytes=18855675
reduction: bytes=66.28%
```

## Pipeline: `topology.compress.topo.bin` (topology-aware simplify + dedup + compress)

### `reducetzpb -topology=true`

```
mode: topology
epsilon: 0.001000
dataset_before: timezones=444 polygons=1322 holes=756 points=8189808 bytes=98293428
dataset_after:  timezones=444 polygons=1322 holes=756 points=1117130 bytes=13420808
dataset_reduction: points=86.36% bytes=86.35%
topology_rings: total=2078 no_fixed=1485 one_fixed=39 multi_fixed=550 fallback=207
topology_points: input=8186335 snapped_inserted=98 fallback_points=10712 fixed_vertices=185657
topology_segments: total=187140 shared=4170(2.23%) skipped_short=182817(97.69%) cache_hits=2077 cache_misses=2093 cache_hit_rate=49.81%
topology_segment_points: input=8373463 output=1292120 reduction=84.57%
topology_segment_length_buckets: le10=183203 le25=332 le50=342 le100=448 gt100=2815
```

### `deduplicatetzpb`

```
input:  timezones=444 polygons=1322 holes=756 points=1117130 bytes=13420815
output: shared_edges=2907 shared_points=467906 inline_segs=183838 edge_ref_segs=5592 bytes=10959070
reduction: bytes=18.34%
dedup_rate: 2.95% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=10959070
output: bytes=6858084
reduction: bytes=37.42%
```

## Pipeline: `topology.preindex.bin` (topology-aware simplify + tile pre-index)

### `preindextzpb`

```
input:  timezones=444 bytes=13420815
params: idxZoom=13 aggZoom=3 maxZoomLevelToKeep=10 layerDrop=2
output: total_keys=88913 bytes=2053657
```

