~ "git: github.com/amatgil/steal-gift" ~ AoCGet
Input ← AoCGet 2016 1

Part₁ ← (
  °/$"_, _"                    ## ["R2"│"L3"] 
  \×≡(⊃(⍣(i°@L|¯i°@R)⊢|⋕↘1)°□) ### [2 3]  
                               ### [¯i 1] 
  × ⊂ 1 ↘ 1 ↻ ¯ 1              ## [2 ¯3i] 
  + °⊟ ⌵ ⊟ °ℂ /+               ## 5 
)

⍤⤙≍ 5 Part₁ "R2, L3" # test
# ⍤⤙≍ 2 Part₁ "R2, R2, R2"      # test
# ⍤⤙≍ 12 Part₁ "R5, L5, R5, R3" # test
# $"Part one solution is: '_'" Part₁ Input # main
# Input
