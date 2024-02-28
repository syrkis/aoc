F ← &fras "2023/input/day01.txt" # read input file
I ← ⊜□ ¬ ⌕ "\n" . F              # make it onto an array of boxes

# part one
D ← ♭ ∵$"_ " ⇡ 10                  # array of numbers to compare against
G ← (⋕ ⊏ ⇌ ⊂ ⊢ ⇌ : ⊢ . ⊚ ∊ , D °□) # unbox, stack D, copy sample, index
/+∵G I

# part two
S ← ⊂ D "one two three four five six seven eight nine zero"
S
