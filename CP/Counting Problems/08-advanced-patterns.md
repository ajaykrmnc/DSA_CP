# Advanced Counting Patterns

These patterns appear when input size or structure rules out the basic approaches.

## Meet In The Middle

Use this when `n` is around 35 to 45.

Idea:

```text
Split array into two halves.
Generate all subset sums for each half.
Combine the two lists with sorting, binary search, or two pointers.
```

Why:

```text
2^40 is too large
2^20 + 2^20 is manageable
```

Common use:

- count subsets with sum `<= K`
- closest subset sum
- subset sum existence for medium `n`

## Bitmask DP / SOS DP

Use this when:

- bits are usually `<= 20`;
- states are masks;
- the problem asks about subsets or supersets.

Common state:

```text
dp[mask] = number of ways to build this selected set
```

SOS DP clue:

```text
For every mask, need sum of freq[submask].
```

SOS DP reduces this from repeated submask loops to:

```text
O(bits * 2^bits)
```

## DSU / Union Find

Use this when counting connected components under merge operations.

Common clues:

- connected components
- groups
- roads
- islands
- merge sets

Example:

```text
n = 5
edges = (1, 2), (3, 4)

components = {1, 2}, {3, 4}, {5}
answer = 3
```

If counting pairs across different components:

```text
total pairs - pairs inside each component
```

## Trie Counting

Use trie for:

- prefix counting in strings;
- dictionary matching;
- autocomplete;
- maximum/minimum XOR;
- counting pairs with XOR constraints.

XOR example:

```text
Insert binary representation of previous numbers.
For maximum XOR with x, greedily choose the opposite bit if available.
```

## Binary Search On Answer

Use this when the problem asks for an optimum value and feasibility is monotonic.

Common clues:

- minimize the maximum
- maximize the minimum
- minimum time
- maximum possible value
- can we do it with X?

Example:

```text
check(T) = can all jobs finish within time T?
If yes, try smaller T.
If no, try larger T.
```

Counting often appears inside `check`.

## Practice Problems

1. LeetCode 1755 - Closest Subsequence Sum
2. LeetCode 805 - Split Array With Same Average
3. LeetCode 847 - Shortest Path Visiting All Nodes
4. LeetCode 1125 - Smallest Sufficient Team
5. LeetCode 698 - Partition to K Equal Sum Subsets
6. LeetCode 1312 - Minimum Insertion Steps to Make a String Palindrome
7. LeetCode 547 - Number of Provinces
8. LeetCode 200 - Number of Islands
9. LeetCode 1707 - Maximum XOR With an Element From Array
10. LeetCode 421 - Maximum XOR of Two Numbers in an Array
11. CSES - Meet in the Middle
12. CSES - Hamiltonian Flights
13. CSES - School Dance
14. Codeforces - Mocha and Diana

