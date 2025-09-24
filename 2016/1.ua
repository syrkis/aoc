~ "git: github.com/amatgil/steal-gift" ~ AoCGet
Input ← AoCGet 2016 1

Part₁ ← (
  °/$"_, _"                  ## ["R5"│"L5"│"R5"│"R3"] 
  ≡(⊃(⋕↘1|⍣(¯i°@R|i°@L)⊢)°□) ## [5 5 5 3] 
  °ℂ /+×⊂1↘1↻¯1\+:           ## ¯8 
)

Part₁ "R5, L5, R5, R3" # tes

# ⍤⤙≍ 5 Part₁ "R2, L3" # test
# ⍤⤙≍ 2 Part₁ "R2, R2, R2"      # test
# ⍤⤙≍ 12 Part₁ "R5, L5, R5, R3" # test
# $"Part one solution is: '_'" Part₁ Input # main
# Input
