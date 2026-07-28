# Pattern Identification Checklist

Counting problems usually ask for the number of valid subarrays, pairs, subsequences, subsets, paths, intervals, masks, or arrangements.

The first goal is to rewrite the condition into a known form.

## Quick Table

| You see | Think |
|---|---|
| `sum == K`, `balance == 0`, `count == K` | Prefix sum + hashmap |
| `xor == K` | Prefix XOR + hashmap |
| `sum <= K`, `sum >= K`, range sum, average, ratio | Prefix values + ordered structure |
| "at most K" with monotonic window | Sliding window |
| "exactly K" | `atMost(K) - atMost(K - 1)` |
| sorted array + pairs/triples | Two pointers |
| equal values, complements, duplicates | Frequency counting |
| nearest greater/smaller | Monotonic stack |
| sliding maximum/minimum | Monotonic queue |
| intervals/events/overlap | Sweep line |
| huge values but only ordering matters | Coordinate compression |
| `n` around 35 to 45 | Meet in the middle |
| masks/subsets/bits <= 20 | Bitmask DP / SOS DP |
| connected components | DSU / Union Find |
| words like "ways", "arrangements", "choose" | DP / combinatorics |

## Decision Flow

1. What object is counted: subarray, pair, subset, path, interval, or arrangement?
2. Can the condition be expressed using a prefix value?
3. After rearranging, is it equality or inequality?
4. If equality, can a hashmap count previous exact states?
5. If inequality, do previous states need ordering?
6. Is the window condition monotonic?
7. Does "exactly K" become `atMost(K) - atMost(K - 1)`?
8. Is sorting allowed without changing the meaning?
9. Are values too large for direct indexing?
10. Are there overlapping intervals or events?
11. Is the input size small enough for masks or meet in the middle?

## Common Mistakes

1. Using sliding window for sum constraints when negative numbers exist.
2. Forgetting `freq[0] = 1` in prefix-counting problems.
3. Using a hashmap for inequality queries.
4. Using floating point for ratio comparisons.
5. Forgetting coordinate compression before using Fenwick tree on large or negative values.
6. Counting intervals incorrectly when start and end events share the same coordinate.

