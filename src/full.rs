/// Full-precision TZF embedded-binary timezone data (`.tzb`, E profile,
/// FUZZY preindex included).
///
/// Only available via git dependency — `src/full.rs` and the underlying
/// binary are excluded from the crates.io package for size.
pub fn load_full_tzb() -> &'static [u8] {
    include_bytes!("../full.tzb")
}
