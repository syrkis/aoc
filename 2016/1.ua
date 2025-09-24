~ "git: github.com/amatgil/steal-gift" ~ AoCGet
Input ← AoCGet 2016 1

Part₁ ← (
  °/$"_, _"                  # ["R2"│"L3"]
  ≡(⊃(⋕↘1|⍣(¯i°@R|i°@L)⊢)°□) # [2 3]
  /+⌵ ⊟ °ℂ /+ × ↘ 1 \×⊂ i :  # 5
)

Part₂ ← (
  °/$"_, _"                  ## ["R8"│"R4"│"R4"│"R8"] 
  ≡(⊃(⋕↘1|⍣(¯i°@R|i°@L)⊢)°□) ## [8 4 4 8] 
  ⍉⊟ ≡°ℂ\+ × ↘ 1 \×⊂ i :     ## ╭─       
                             ## ╷  0 8   
                             ##   ¯4 8   
                             ##   ¯4 4   
                             ##    4 4   
                             ##        ╯ 
)

Part₂"R8, R4, R4, R8" # tes
# Part₁ "R2, R2, R2" # tes

# ⍤⤙≍ 5 Part₁ "R2, L3" # test
# ⍤⤙≍ 2 Part₁ "R2, R2, R2"                 # test
# ⍤⤙≍ 12 Part₁ "R5, L5, R5, R3"            # test
# $"Part one solution is: '_'" Part₁ Input # main
