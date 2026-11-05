DataCet ≁ "datacet.ua"
⍤ "different amount of ids and filenames" =∩⧻ DataCet.Ids DataCet.Filenames

# Track caller!
GetFilename ↚ °□⍣(⊙◌˜⊡|˜⍤0⋅⋅$"could not find color map _")DataCet.Filenames⊗DataCet.Ids⊸□
GetClass    ↚ ⊡-₁⊢⊚⊸(↧⊃(≥@0|≤@9))

# Track caller!
# ? id
LoadColors ← |1 ≡₀(⋕°□)°csv&fras $"__CETperceptual\_csv\_0\_1__" ThisFileDir pathsep pathsep GetFilename

# Track caller!
# ? id data
# Turns data within the 0-1 range into colors using the color set specified with the `id` argument
Sample ← |2 /+×⊓˜⊏(⊟⤙˜-1)⊓LoadColors(⊟↧255⊸+₁⌊⤙-⊸⌊×255↥0↧1)

# ? id data
# Attempts to map `data` to 0-1 based on `id`.
# 
# If `id` is a cyclic color map, it assumes the data is angular and divides by τ and forces it into a 0-1 range
# If `id` is a diverging color map, it assumes it is in the range ¯1-1
# Otherwise, it ignores it
Format ← ⍣(◿1÷τ°@C|÷2+1°@D|◌)GetClass

# Track caller!
# ? id data
# Equivalent to `Cet.Sample⟜Cet.Format`
Call ← Sample⟜Format
