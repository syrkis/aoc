~ "git: github.com/amatgil/steal-gift" ~ AoCGet

# ====== INPUTS ======
Input ← AoCGet 2015 3

Part₁ ← (
  ≡⍣(1_0°@^|0_1°@>|¯1_0°@v|0_¯1°@<) #  parse
  +1/+ ⧆₁ /+ ⍉ × ¤ 1_100 \+         # uniques
)
Part₁Input

Part₂ ← (
  ≡⍣(1_0°@^|0_1°@>|¯1_0°@v|0_¯1°@<) #  parse
  ↙ 10
  ⊸↻1◿₂⇡ ⊸⧻
  ⊙⊏:⊸⊙⊏⊙⊚⊚
)
Part₂Input
