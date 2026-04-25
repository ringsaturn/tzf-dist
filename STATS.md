# Build Statistics

**Version:** 2026a
**Build date:** 2026-04-25T15:05:28Z

## Output Files

| File | Size | MD5 |
|------|------|-----|
| `combined-with-oceans.compress.topo.bin` | 16.7 MB | `4728f59f7823eafa77f1dbb9b0c6a5f6` |
| `combined-with-oceans.topology.compress.topo.bin` | 5.4 MB | `571b39083336a6bc1cdd0919efeaf356` |
| `combined-with-oceans.topology.preindex.bin` | 2.0 MB | `d31bd6a73072e1a0d2c7341234b2cfc6` |

## Pipeline: `compress.topo.bin` (dedup + compress on full precision)

### `deduplicatetzpb`

```
input:  timezones=444 polygons=1323 holes=755 points=8024568 bytes=96310559
output: shared_edges=3526 shared_points=4106169 inline_segs=170426 edge_ref_segs=5604 bytes=54642952
reduction: bytes=43.26%
dedup_rate: 3.18% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=54642952
output: bytes=17496532
reduction: bytes=67.98%
```

## Pipeline: `topology.compress.topo.bin` (topology-aware simplify + dedup + compress)

### `reducetzpb -topology=true`

```
mode: topology
epsilon: 0.001000
dataset_before: timezones=444 polygons=1323 holes=755 points=8024568 bytes=96310552
dataset_after:  timezones=444 polygons=1323 holes=755 points=1094619 bytes=13150673
dataset_reduction: points=86.36% bytes=86.35%
topology_rings: total=2078 no_fixed=1487 one_fixed=39 multi_fixed=547 fallback=206
topology_points: input=8021086 snapped_inserted=100 fallback_points=10687 fixed_vertices=172223
topology_segments: total=173705 shared=4164(2.40%) skipped_short=169391(97.52%) cache_hits=2074 cache_misses=2090 cache_hit_rate=49.81%
topology_segment_points: input=8194776 output=1256196 reduction=84.67%
topology_segment_length_buckets: le10=169765 le25=335 le50=347 le100=452 gt100=2806
```

### `deduplicatetzpb`

```
input:  timezones=444 polygons=1323 holes=755 points=1094619 bytes=13150680
output: shared_edges=2894 shared_points=463358 inline_segs=170404 edge_ref_segs=5568 bytes=10527421
reduction: bytes=19.95%
dedup_rate: 3.16% of segments reference shared edges
```

### `compresstopotzpb`

```
input:  bytes=10527421
output: bytes=5700013
reduction: bytes=45.86%
```

## Pipeline: `topology.preindex.bin` (topology-aware simplify + tile pre-index)

### `preindextzpb`

```
input:  timezones=444 bytes=13150680
params: idxZoom=13 aggZoom=3 maxZoomLevelToKeep=10 layerDrop=2
output: total_keys=88867 bytes=2052271
```

