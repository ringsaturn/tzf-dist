/// Memory-image profile of the lite dataset (`.tzm`, M profile): the file
/// *is* the query-time structure, so a reader can alias its ring storage in
/// place instead of decoding.
///
/// Only available via git dependency — `src/tzm.rs` and the underlying
/// binary are excluded from the crates.io package for size. Derivable from
/// `lite.tzb` with tzf's `tzb2tzm`; never distributed beyond this repo.
pub fn load_lite_tzm() -> &'static [u8] {
    include_bytes!("../lite.tzm")
}
