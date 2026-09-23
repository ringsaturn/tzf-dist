/// Compact TZF embedded-binary timezone data (`.tzb`, E profile, FUZZY
/// preindex included). Format: TZF embedded binary 1.1 — parse with tzf-rs
/// or any reader of the spec. Backs the lite finders.
pub fn load_lite_tzb() -> &'static [u8] {
    include_bytes!("../lite.tzb")
}

#[cfg(feature = "full")]
mod full;
#[cfg(feature = "full")]
pub use full::load_full_tzb;
