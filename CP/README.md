# Competitive Programming Notes

This folder is organized by problem-solving pattern. Prefer starting from the pattern guides before jumping into individual problem notes.

## Core Pattern Guides

| Topic | Use When |
|---|---|
| [Introductory Problems](<Introductory Problems/README.md>) | CSES basics: formulas, simulation, recursion, simple construction |
| [Counting Problems](<Counting Problems/README.md>) | Count subarrays, pairs, subsets, paths, intervals, or arrangements |
| [Binary Search](<Binary Search/README.md>) | Need exact value, first/last valid position, or binary search on answer |
| [Divide And Conquer](<Divide and Conquer/README.md>) | Split ranges recursively, merge answers, count cross-pairs, or optimize monotonic DP |
| [MEX](<MEX/README.md>) | Control missing small values, prefix/range mex, and dynamic mex |
| [Permutation](<Permutation/README.md>) | Arrange unique values, handle position constraints, cycles, inversions, and swaps |
| [Binary Indexed Tree](<Binary Indexed Tree/README.md>) | Need dynamic prefix sums, ordered counts, inversion count, or compressed frequency queries |
| [Segment Tree](<Segment Tree/README.md>) | Need range queries with updates or richer node information |
| [Range Query Advanced](<Range Query Advanced/README.md>) | Sparse table, offline queries, Mo's algorithm, persistence, order queries |
| [Two Pointer](<Two_Pointer/README.md>) | Sorted pairs, sliding windows, slow/fast pointers, or in-place compaction |
| [String](<String/README.md>) | String matching, windows, parsing, trie, DP, or hashing |
| [Geometry](<Geometry/README.md>) | Cross product, intersections, polygon area, convex hull, distance |
| [Interval Problems](<Interval Problem/README.md>) | Merge ranges, count overlaps, sweep events, or allocate rooms/groups |
| [Parentheses](<Parentheses/README.md>) | Stack, balance, locked brackets, removal, or generation |
| [Backtracking](<Backtracking/README.md>) | Generate combinations, subsets, permutations, paths, boards, or constrained assignments |
| [DP](<DP/README.md>) | Count or optimize using reusable states |
| [Graph](<LT_GRAPH/README.md>) | Traversal, shortest paths, DSU, MST, graph DP, or components |
| [Number Theory](<Number Theory/README.md>) | Divisibility, gcd/lcm, primes, factorization, modular arithmetic, or inclusion-exclusion |
| [Bit Manipulation](<Bit Manipulation/README.md>) | Masks, XOR, bit tricks, subset iteration, or bitwise DP |
| [Constructive Problems](<Construction Problems/README.md>) | Build any valid object using invariants, parity, greedy placement, grids, graphs, and operation sequences |
| [Interactive Problems](<Interactive Problems/README.md>) | Query budget, flushing, interaction strategy, hidden data reconstruction |
| [Sqrt Decomposition](<Sqrt Decomposition/README.md>) | Block decomposition, small/large splits, and offline range queries |

## How To Use This Repo

1. Identify the pattern from the statement.
2. Read the relevant folder `README.md`.
3. Solve 2-3 listed practice problems from that pattern.
4. Then open individual notes for implementation details.

## Common Gaps To Watch

1. If a problem asks for exact equality on subarrays, check prefix hashmap patterns.
2. If it asks for inequality on prefixes, check Fenwick/segment tree patterns.
3. If it asks for minimum/maximum possible answer, check binary search on answer.
4. If it asks for pairs across left/right halves, inversion-like counting, or kth selection, check divide and conquer.
5. If it asks for mex or missing small values, check MEX.
6. If it asks for unique orderings, permutation positions, swaps, or cycles, check Permutation.
7. If it asks for range query with updates, compare Fenwick vs segment tree.
8. If the input has masks or subset constraints, check bit manipulation and bitmask DP.
9. If it uses geometry words, reduce the condition to cross product or distance comparisons.
10. If it asks for many string matches, use KMP/Z/Aho-Corasick/suffix structures instead of nested loops.
11. If it asks to generate all valid objects or find a constrained assignment with small constraints, check backtracking.
