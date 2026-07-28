# CSES Pattern Gap Analysis

This note compares the repo against CSES-style topic coverage and highlights missing or weak pattern areas.

## Fill Status

The major gaps from this audit now have starter pattern folders:

- [Geometry](Geometry/README.md)
- [String Algorithms](String/README.md)
- [Advanced Graph](LT_GRAPH/Advanced%20Graph/README.md)
- [Range Query Advanced](Range%20Query%20Advanced/README.md)
- [Advanced Tree Techniques](LT_GRAPH/Tree%20Graph/09%20Advanced%20Tree%20Techniques/README.md)
- [Construction Problems](Construction%20Problems/README.md)
- [Interactive Problems](Interactive%20Problems/README.md)
- [Advanced Combinatorics And Recurrences](Number%20Theory/06-Advanced%20Combinatorics%20and%20Recurrences/README.md)
- [Bit Manipulation Advanced Subsections](Bit%20Manipulation/README.md)

## Summary

The repo already has good coverage for:

- counting patterns;
- binary search;
- two pointers and sliding windows;
- DP families;
- basic graph traversal;
- shortest paths;
- DSU and MST;
- Fenwick tree;
- segment tree;
- tree basics, LCA, diameter, rerooting, and tree DP;
- number theory basics;
- interval and sweep-line basics.

The main missing CSES-level pattern families are:

1. computational geometry;
2. formal string algorithms;
3. advanced graph algorithms;
4. persistent/offline range-query techniques;
5. advanced tree decomposition techniques;
6. construction and interactive problem patterns;
7. deeper combinatorics and linear recurrences.

## Gap Table

| CSES Area | Repo Coverage | Gap Level | Missing Patterns |
|---|---|---:|---|
| Introductory Problems | Scattered across DSA/CP | Medium | CSES-specific implementation, recursion, bit generation, backtracking basics |
| Sorting and Searching | Good | Low | Greedy scheduling with multiset, order-statistics set, Josephus variants |
| Sliding Window Problems | Present inside Counting/Two Pointer | Low | Dedicated CSES sliding-window checklist |
| Dynamic Programming | Strong | Low | Counting tilings/profile DP could be stronger |
| Graph Algorithms | Good basics | Medium | SCC, 2-SAT, Euler tour/path, functional graph patterns |
| Advanced Graph Problems | Weak | High | max flow, min cut, bipartite matching, min-cost flow, dominator-like thinking |
| Range Queries | Good basics | Medium | persistent segment tree, sparse table, offline queries, Mo's algorithm |
| Tree Algorithms | Good basics | Medium | centroid decomposition, DSU on tree, heavy-light decomposition, virtual tree |
| Mathematics | Medium | Medium | matrix exponentiation, linear recurrences, stars and bars, Burnside, advanced modular combinatorics |
| String Algorithms | Weak | High | KMP, Z-function, Manacher, suffix array, suffix automaton, Aho-Corasick |
| Geometry | Missing | High | orientation, convex hull, polygon area, line intersection, closest pair |
| Bitwise Operations | Basic guide exists | Medium | XOR basis, bit DP, subset transforms |
| Construction Problems | Scattered | Medium | constructive proof patterns, invariant construction, parity construction |
| Counting Problems | Recently added | Low | CSES-specific problem mapping can be added later |
| Interactive Problems | Missing | Medium | query strategy, binary-search interaction, flushing, adversarial protocols |

## Highest Priority Missing Folders

### 1. Geometry

Create:

```text
CP/Geometry/
```

Subsections to add:

1. Points, vectors, dot product, cross product
2. Orientation and segment intersection
3. Polygon area and Pick's theorem
4. Convex hull
5. Closest pair of points
6. Line sweep geometry basics

CSES problems to map:

- Point Location Test
- Line Segment Intersection
- Polygon Area
- Point in Polygon
- Polygon Lattice Points
- Minimum Euclidean Distance
- Convex Hull
- Maximum Manhattan Distances
- All Manhattan Distances
- Intersection Points
- Line Segments Trace I
- Line Segments Trace II
- Lines and Queries I
- Lines and Queries II
- Area of Rectangles
- Robot Path

### 2. String Algorithms

Current `CP/String` has useful LeetCode notes, but it lacks the core CSES string-algorithm toolkit.

Add subsections:

1. Prefix function / KMP
2. Z-function
3. Rolling hash
4. Manacher
5. Trie and Aho-Corasick
6. Suffix array
7. Suffix automaton

CSES problems to map:

- Word Combinations
- String Matching
- Finding Borders
- Finding Periods
- Minimal Rotation
- Longest Palindrome
- All Palindromes
- Required Substring
- Palindrome Queries
- Finding Patterns
- Counting Patterns
- Pattern Positions
- Distinct Substrings
- Distinct Subsequences
- Repeating Substring
- String Functions
- Inverse Suffix Array
- String Transform
- Substring Order I
- Substring Order II
- Substring Distribution

### 3. Advanced Graph

Your graph folder covers traversal, DSU, MST, shortest paths, and graph DP well. Missing advanced CSES graph patterns should be separated.

Create:

```text
CP/LT_GRAPH/Advanced Graph/
```

Subsections to add:

1. SCC with Kosaraju/Tarjan
2. Condensation DAG
3. 2-SAT
4. Eulerian path/circuit
5. Functional graphs
6. Max flow with Dinic
7. Bipartite matching
8. Min cut modeling

CSES problems to map:

- Planets Queries I
- Planets Queries II
- Planets Cycles
- Course Schedule
- Round Trip II
- Coin Collector
- Giant Pizza
- Mail Delivery
- De Bruijn Sequence
- School Dance
- Distinct Routes

### 4. Persistent And Offline Range Queries

Your Fenwick/segment tree coverage is good for standard dynamic queries. CSES advanced range-query problems need more.

Add subsections:

1. Sparse table
2. Offline queries with sorting
3. Mo's algorithm
4. Persistent segment tree
5. Wavelet tree basics
6. Ordered set / policy-based data structures

CSES problems to map:

- Static Range Minimum Queries
- Distinct Values Queries
- Distinct Values Queries II
- Range Queries and Copies
- Range Interval Queries
- Movie Festival Queries
- Missing Coin Sum Queries

### 5. Advanced Tree Techniques

Your tree graph folder has strong basics and rerooting. Missing CSES-hard tree patterns:

1. Centroid decomposition
2. DSU on tree / small-to-large
3. Heavy-light decomposition
4. Euler tour + Fenwick/segment tree for subtree/path
5. Virtual tree
6. Binary lifting with path aggregates

CSES problems to map:

- Counting Paths
- Path Queries
- Path Queries II
- Distinct Colors
- Fixed-Length Paths I
- Fixed-Length Paths II
- Finding a Centroid

### 6. Construction Problems

Construction problems need a different checklist from normal algorithm selection.

Create:

```text
CP/Construction Problems/
```

Patterns to add:

1. Invariant-based construction
2. Parity construction
3. Greedy placement
4. Symmetric construction
5. Reverse operation construction
6. Impossibility proofs

CSES problems to map:

- Permutations
- Two Sets
- Gray Code
- Mex Grid Construction
- Grid Coloring I
- Additional construction-style problems

### 7. Interactive Problems

Interactive problems are absent. Even if you do not practice them often, a small guide is useful.

Create:

```text
CP/Interactive Problems/
```

Patterns to add:

1. Query budget analysis
2. Binary-search interaction
3. Information gain per query
4. Flushing output
5. Handling invalid judge replies
6. Strategy simulation before implementation

## Medium Priority Gaps

### Bitwise Operations

Already has a guide, but CSES-level bitwise coverage should add:

- XOR basis;
- subset convolution basics;
- fast Walsh-Hadamard transform idea;
- SOS DP as a standalone note;
- bitwise trie for XOR constraints.

CSES-style problems to map:

- Hamming Distance
- Beautiful Subgrids
- Reachable Nodes
- Reachability Queries
- One Bit Positions

### Mathematics

The number theory folder is useful, but add:

- modular inverse and factorial precomputation as a standalone guide;
- stars and bars;
- Catalan numbers;
- Burnside's lemma;
- matrix exponentiation;
- linear recurrences;
- game theory with Grundy numbers.

### Introductory Problems

Create a small CSES introductory mapping for:

- simulation;
- formula derivation;
- recursion;
- backtracking;
- bit generation;
- simple constructive patterns.

## Recommended Order To Fill Gaps

1. `CP/Geometry`
2. `CP/String Algorithms` or expand `CP/String`
3. `CP/LT_GRAPH/Advanced Graph`
4. `CP/Range Query Advanced`
5. `CP/LT_GRAPH/Tree Graph/09 Advanced Tree Techniques`
6. `CP/Construction Problems`
7. `CP/Interactive Problems`
8. Expand `CP/Bit Manipulation`
9. Expand `CP/Number Theory`

## Practical Next Step

Start with geometry and string algorithms. These are the clearest missing CSES categories and have the least overlap with existing notes.

Suggested first batch:

```text
CP/Geometry/README.md
CP/Geometry/01-points-vectors-cross-product.md
CP/Geometry/02-segment-intersection.md
CP/Geometry/03-polygon-area-lattice-points.md
CP/Geometry/04-convex-hull.md

CP/String/01-kmp-prefix-function.md
CP/String/02-z-function.md
CP/String/03-manacher.md
CP/String/04-suffix-array.md
CP/String/05-aho-corasick.md
```
