/// Full-precision timezone data without topology simplification.
/// Format: `CompressedTopoTimezones` (~17 MB). Use with tzf-rs full finders.
///
/// Only available via git dependency — `src/full.rs` and the underlying binary
/// are excluded from the crates.io package.
pub fn load_compress_topo() -> &'static [u8] {
    include_bytes!("../combined-with-oceans.compress.topo.bin")
}
