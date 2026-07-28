# Counting Problems

This folder is split by counting pattern. Start with the identification guide, then study one subsection at a time.

## Subsections

1. [Pattern Identification Checklist](01-pattern-identification.md)
2. [Prefix Equality Counting](02-prefix-equality.md)
3. [Prefix Inequality Counting](03-prefix-inequality.md)
4. [Sliding Window Counting](04-sliding-window.md)
5. [Pair And Frequency Counting](05-pair-frequency-two-pointers.md)
6. [Ordering And Interval Counting](06-ordering-intervals.md)
7. [Combinatorics And DP Counting](07-combinatorics-dp.md)
8. [Advanced Counting Patterns](08-advanced-patterns.md)

## Recommended Study Order

1. Prefix sum + hashmap
2. Prefix XOR + hashmap
3. Sliding window
4. Exactly K from at most K
5. Frequency counting and two pointers
6. Fenwick tree for prefix inequalities
7. Monotonic stack, monotonic queue, and sweep line
8. Combinatorics, DP counting, and inclusion-exclusion
9. Meet in the middle, bitmask DP, trie, and DSU

## Main Corrections From The Raw Notes

1. Prefix XOR uses `pref[r] ^ pref[l - 1] = K`, so the previous prefix needed is `pref[r] ^ K`.
2. Equality counting usually needs a hashmap.
3. Inequality counting needs ordered counts: Fenwick tree, segment tree, balanced BST, or sorting.
4. Sliding window needs a monotonic condition.
5. Average and ratio problems should be converted into linear inequalities before choosing the data structure.
6. `exactly(K) = atMost(K) - atMost(K - 1)` works when the `atMost` version is monotonic and easy to count.

