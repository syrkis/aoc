~ "git: github.com/amatgil/steal-gift" ~ AoCGet

# ====== INPUTS ======
Input ← AoCGet 2015 2

# ====== 2015 2 ======
Part₁ ← (
  ⋕ ⊜□ ⊸≠@x            # numbers to array
  > 0 ◿ 4 ↯ 3_3 ⇡ 9    # iterations
  + ˜- 1 ⟜(⍉ ≡₃×)      # somehing
  + × 2 : ⊃(⊢⍆|/+) ≡/× # something else
)

/+≡(Part₁°□)⊜□⊸≠@\nInput

Part₂ ← (
  ⋕ ⊜□ ⊸≠@x # parse
  ⟜/×
  ↙ 2 ⍆
  .
  ♭ ⊟
  /+
  +
)
/+≡(Part₂°□)⊜□⊸≠@\nInput
# ⊃Part₁Part₂Input

# "2x3x4"
# Part₁

# ⊃⊃(2 × ×|2××|2××)

# ⊂ A₂ C₂
