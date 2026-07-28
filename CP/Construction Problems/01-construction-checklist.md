# Construction Checklist

Use this checklist before coding a constructive problem. The goal is to reduce guessing: first find the constraints that cannot be violated, then design a pattern that satisfies all remaining rules.

## 1. Find Necessary Conditions

Ask:

- does parity matter?
- does total sum need to be divisible?
- are there lower/upper bounds?
- is a graph degree sequence possible?
- is a permutation constraint impossible for small `n`?
- does every operation preserve xor, gcd, multiset size, number of inversions, or connected components?
- does every row/column/cell need a minimum number of choices?

Example:

```text
Split 1..n into two equal-sum sets.
Total = n * (n + 1) / 2
If total is odd, impossible.
```

Necessary conditions are only the first filter. They are not always sufficient. After finding them, test whether a construction can always satisfy them.

## 2. Build Small Cases By Hand

Before coding, write valid answers for small inputs:

```text
n = 1
n = 2
n = 3
n = 4
n = 5
n = 6
```

Look for:

- parity split;
- repeating block;
- high/low alternation;
- cyclic shift;
- diagonal or checkerboard grid pattern;
- one exceptional small value.

If the pattern starts working from some threshold, prove the threshold and hardcode the smaller cases.

## 3. Try Greedy Construction

Common greedy constructions:

- place largest values first;
- alternate high and low values;
- fill by parity;
- build from the end backwards.
- satisfy the most constrained position first;
- fill boundaries before the middle;
- sort requirements and assign smallest possible value that works.

Greedy is strongest when you can prove that each step leaves a similar smaller problem.

## 4. Reverse The Operation

If forward operations are hard, ask:

```text
Can I construct the final state, then reverse operations?
```

This is common in graph, array, and game construction.

Examples:

- delete operations become add operations;
- merging components becomes splitting components;
- reducing a number becomes expanding it;
- sorting by swaps can be built by reversing the desired swaps.

## 5. Choose A Known Shape

Many constructions come from a small set of shapes.

| Object | Useful Shapes |
|---|---|
| array/permutation | sorted blocks, parity blocks, cyclic shifts, alternating extremes |
| string | repeating block, balanced counts, greedy lexicographic fill |
| grid | checkerboard, diagonals, snake order, layers, transpose symmetry |
| graph | path, star, cycle, tree, clique, complete bipartite graph |
| operations | reverse process, simulate target from left to right, normalize then rebuild |

## 6. Handle Small Cases Separately

Many construction problems fail only for small values.

```text
n = 1, 2, 3 often need special handling.
```

Do not push a general formula onto small cases unless it is clearly valid.

## 7. Verify The Output, Not The Idea

After designing the construction, check the exact printed object.

For arrays/permutations:

- all values are inside range;
- no duplicates if permutation is required;
- adjacency and prefix/suffix constraints hold.

For grids:

- dimensions are correct;
- every row and column condition holds;
- every neighbor condition holds;
- corner and border cells are checked separately.

For graphs:

- vertices are inside range;
- no duplicate edges unless allowed;
- degree and connectivity constraints hold;
- edge count is exactly required.

For operations:

- each operation is legal at the time it is applied;
- operation count is within the limit;
- final state matches the target.

## Practice Problems

- CSES - Permutations
- CSES - Two Sets
- CSES - Gray Code
- CSES - Tower of Hanoi
