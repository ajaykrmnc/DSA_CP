# Backtracking Algorithms

Use this folder when the statement requires trying choices and undoing them. Problem files live in pattern folders.

## Pattern Map

| Pattern | Matching signal | Problems |
|---|---|---|
| Subset / combination recursion | Need all unique subsets or sums | [Unique Subsets](<Subset and combination recursion/Unique Subsets.md>), [Combination Sum](<Subset and combination recursion/Combination Sum.md>) |
| Grid path search | Move through a grid under constraints | [Rat Maze With Multiple Jumps](<Grid path search/Rat Maze With Multiple Jumps.md>) |
| Constraint satisfaction | Assign values/colors while checking validity | [Solve the Sudoku](<Constraint satisfaction/Solve the Sudoku.md>), [M-Coloring Problems](<Constraint satisfaction/M-Coloring Problems.md>), [Black and White](<Constraint satisfaction/Black and White.md>) |
| Permutation with pruning | Try swaps/ordering choices and keep best answer | [Largest number in K swaps](<Permutation with pruning/Largest number in K swaps.md>) |

## Pattern Matches

1. **Backtracking + visited state**: Grid and graph-style placement problems.
2. **Backtracking + hashing/sorting**: Duplicate-safe subsets and combinations.
3. **Backtracking + pruning**: Sudoku, graph coloring, and max-number swaps.
4. **Backtracking + greedy bound**: Stop branches that cannot beat the current best.
