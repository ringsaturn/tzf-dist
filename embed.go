package tzfdist

import _ "embed"

// The TZF embedded-binary artifact set backing the github.com/ringsaturn/tzf/v2
// finders. All three files carry the same data_version; the files on the main
// branch are placeholders — real data lives on the data branch, like the
// protobuf artifacts before them.
//
//   - lite.tzb: compact E-profile file with the FUZZY preindex; backs
//     NewEmbeddedFinder (queried in place) and generic TZB use.
//   - lite.tzm: M-profile memory image of lite.tzb; backs NewDefaultFinder
//     (ring storage aliases these bytes in place — see the alignment test).
//   - full.tzb: full-precision E-profile file with FUZZY; backs NewFullFinder.
//
// full.tzm is never distributed; derive it locally with tzb2tzm when needed.

//go:embed lite.tzb
var LiteTZB []byte

//go:embed lite.tzm
var LiteTZM []byte

//go:embed full.tzb
var FullTZB []byte
