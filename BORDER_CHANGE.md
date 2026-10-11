## Evaluation result

- Source input: `../tzf-dist/combined-with-oceans.json`
- Candidate input: `../tzf-dist/combined-with-oceans.topology.compress.topo.gob`
- Source dataset version: `not encoded`
- Candidate dataset version: `2026e`
- Source points after topology normalization: `8284376`
- Candidate points: `1131706`
- Point reduction: `86.339%`
- Unique source arcs: `537827`
- Changed arcs: `522806`
- Original unique boundary length: `1312190.492 km`
- Changed boundary length: `890233.505 km`
- Error strip area: `16442.219423 km2`
- Maximum single strip area: `636.860912 km2`
- Junction vertices inserted by shared-edge deduplication (dropped before arc matching): `50`, maximum offset from the baseline ring: `0.626 m`
- Runtime: `1m56.033s`

### Boundary displacement

| Metric | Distance |
|---|---:|
| Length-weighted p50 | 0.900 m |
| Length-weighted p95 | 65.700 m |
| Length-weighted p99 | 91.900 m |
| Length-weighted p99.9 | 106.500 m |
| Certified maximum | 111.538 m |
| Certification upper tolerance | +1.000 m |

Maximum location: `13.8291607, -4.4331002`, timezone pair: `Africa/Brazzaville` / `Africa/Kinshasa`.

| Threshold | Boundary length above threshold |
|---|---:|
| 10 m | 37.767193% |
| 50 m | 9.613203% |
| 100 m | 0.402863% |
| 500 m | 0.000000% |

### Error strip width

| Metric | Width |
|---|---:|
| Area-weighted p50 | 30.700 m |
| Area-weighted p95 | 529.100 m |
| Area-weighted p99 | 3837.500 m |
| Area-weighted p99.9 | 4714.400 m |

- Error area within 10 m of source boundary: `14.891532%`
- Error area within 50 m of source boundary: `74.733730%`
- Error area within 100 m of source boundary: `92.538453%`

### Largest timezone-pair error areas

| Timezone A | Timezone B | Area |
|---|---|---:|
| Africa/Algiers | Africa/Bamako | 650.814924 km2 |
| Asia/Tokyo | Etc/GMT-9 | 273.033055 km2 |
| Australia/Brisbane | Etc/GMT-10 | 246.360231 km2 |
| Etc/GMT-2 | Europe/Athens | 245.000075 km2 |
| Etc/GMT+10 | Pacific/Tahiti | 238.856118 km2 |
| Australia/Perth | Etc/GMT-8 | 187.784112 km2 |
| Asia/Shanghai | Etc/GMT-8 | 156.494980 km2 |
| America/Nome | Etc/GMT+11 | 152.693521 km2 |
| Etc/GMT-11 | Pacific/Majuro | 139.623076 km2 |
| Etc/GMT+9 | Pacific/Tahiti | 131.579843 km2 |
| America/Iqaluit | America/Toronto | 122.482904 km2 |
| Etc/GMT-11 | Pacific/Noumea | 118.178278 km2 |
| Etc/GMT-10 | Pacific/Chuuk | 116.629052 km2 |
| Etc/GMT-12 | Pacific/Auckland | 109.966976 km2 |
| America/Santiago | Etc/GMT+5 | 108.768766 km2 |
| America/New_York | Etc/GMT+5 | 108.576489 km2 |
| Etc/GMT | Europe/London | 107.996116 km2 |
| Asia/Kolkata | Etc/GMT-5 | 100.803076 km2 |
| America/Cambridge_Bay | America/Rankin_Inlet | 99.316964 km2 |
| Etc/GMT-1 | Europe/Rome | 90.519413 km2 |

