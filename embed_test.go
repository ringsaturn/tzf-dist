package tzfdist

import (
	"testing"
	"unsafe"
)

// TestLiteTZMAlignment pins the 8-byte alignment of the embedded lite.tzm
// bytes (tzf v2 plan W2). The .tzm memory image aliases its FLATPOINTS
// section in place only when the backing slice is 8-byte aligned; on a
// misaligned slice the tzf/v2 loader silently falls back to a one-time
// decoded copy, roughly doubling NewDefaultFinder's memory. The Go toolchain
// currently places go:embed data with sufficient alignment but does not
// document a guarantee, so this test exists to catch a toolchain change
// loudly instead of as a quiet memory regression.
func TestLiteTZMAlignment(t *testing.T) {
	if len(LiteTZM) == 0 {
		t.Fatal("LiteTZM is empty")
	}
	if addr := uintptr(unsafe.Pointer(&LiteTZM[0])); addr%8 != 0 {
		t.Fatalf("embedded lite.tzm is not 8-byte aligned (addr %% 8 = %d): "+
			"tzf/v2 NewFinderFromTZM will engage the copy fallback and retain "+
			"roughly twice the memory", addr%8)
	}
}

// TestArtifactsPresent guards against an embed directive silently matching a
// missing or truncated file set.
func TestArtifactsPresent(t *testing.T) {
	for name, data := range map[string][]byte{
		"lite.tzb": LiteTZB,
		"lite.tzm": LiteTZM,
		"full.tzb": FullTZB,
	} {
		if len(data) == 0 {
			t.Errorf("%s: embedded data is empty", name)
		}
	}
}
