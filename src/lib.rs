/// Topology-aware simplified + shared-edge dedup + polyline compressed timezone data.
/// Format: `CompressedTopoTimezones` (~5.4 MB). Use with tzf-rs lite/full finders.
pub fn load_topology_compress_topo() -> &'static [u8] {
    include_bytes!("../combined-with-oceans.topology.compress.topo.bin")
}

/// Tile pre-index for fast fuzzy timezone lookup.
/// Format: `PreindexTimezones` (~2 MB). Use with tzf-rs FuzzyFinder.
pub fn load_preindex() -> &'static [u8] {
    include_bytes!("../combined-with-oceans.topology.preindex.bin")
}
