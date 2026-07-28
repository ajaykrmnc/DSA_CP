# Bit Manipulation

Bit manipulation problems use binary representation directly. The main skill is to convert the statement into one of
these forms:

- a bit is present or absent;
- XOR cancels equal values;
- each bit contributes independently;
- a subset can be represented by a mask;
- parity can be represented by one bit;
- values can be processed as binary vectors.

## Quick Operations

```cpp
bool has = x & (1LL << b);
x |= (1LL << b);        // set bit b
x &= ~(1LL << b);       // clear bit b
x ^= (1LL << b);        // toggle bit b
long long low = x & -x; // lowest set bit
x &= x - 1;             // remove lowest set bit
```

Use `1LL << b` when `b >= 31`.

## Pattern Map

| Pattern | Use When | Main Idea |
|---|---|---|
| Core bit tricks | Need test/set/remove bits, powers of two, popcount | Manipulate one bit or lowest set bit |
| XOR cancellation | Equal values disappear, one/two missing values, prefix XOR | `x ^ x = 0` |
| Bit count modulo k | One value appears once, others appear `k` times | Count each bit modulo `k` |
| Prefix XOR | Query subarray XOR or count subarrays with XOR `k` | `xor(l..r) = pref[r] ^ pref[l - 1]` |
| Bit contribution | Sum/count over all pairs/subarrays with XOR/AND/OR | Solve each bit separately |
| Binary trie | Need maximum/minimum XOR with another value | Greedy from highest bit |
| Mask DP | `n <= 20`, subset is the state | `dp[mask]` |
| Submask iteration | Need all subsets of a chosen mask | `(sub - 1) & mask` |
| SOS DP | Need sums over all submasks/supermasks for every mask | `O(n * 2^n)` transform |
| XOR basis | Need maximum subset XOR or count distinct subset XORs | Gaussian elimination over bits |
| Parity masks | Odd/even frequency matters | Toggle one bit per character/value |
| Bitsets | Many boolean states need fast AND/OR/count | Pack booleans into machine words |
| Range bitwise | Range AND/OR or bitwise constraints | Bits are monotonic or independent |

## Identification Checklist

Choose bit manipulation when:

- constraints contain `n <= 20`, `2^n`, or values up to `2^60`;
- operations are XOR, AND, OR, shifts, or bit counts;
- the statement asks for subsets, parity, Hamming distance, or masks;
- pair/subarray sums can be decomposed bit by bit;
- a CSES-style solution expects short loops over `0..LOG`.

## Subsections

1. [Core Bit Tricks](04-core-bit-tricks.md)
2. [XOR Cancellation And Prefix XOR](05-xor-cancellation-prefix.md)
3. [Bit Contribution Counting](06-bit-contribution-counting.md)
4. [Maximum XOR Trie](07-maximum-xor-trie.md)
5. [Mask DP And Submask Iteration](08-mask-dp-submask.md)
6. [XOR Basis](01-xor-basis.md)
7. [SOS DP](02-sos-dp.md)
8. [Parity Masks And Bitsets](03-parity-masks-and-bitsets.md)
9. [Range Bitwise Queries](09-range-bitwise-queries.md)

## Practice Problems

- CSES - Counting Bits
- CSES - Hamming Distance
- CSES - Beautiful Subgrids
- CSES - Hamiltonian Flights
- CSES - Elevator Rides
- LeetCode 136 - Single Number
- LeetCode 137 - Single Number II
- LeetCode 260 - Single Number III
- LeetCode 318 - Maximum Product of Word Lengths
- LeetCode 421 - Maximum XOR of Two Numbers in an Array
- LeetCode 1707 - Maximum XOR With an Element From Array
- LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
- LeetCode 1879 - Minimum XOR Sum of Two Arrays
- LeetCode 1915 - Number of Wonderful Substrings
- Codeforces - XOR basis and subset DP problems

## Existing Notes

- [1707 Maximum XOR With an Element From Array](<1707 Maximum XOR With an Element From Array.md>)
- [monotonic-and-xor-sparse-matrix](monotonic-and-xor-sparse-matrix.md)
- [sparse-matrix-implementation-details](sparse-matrix-implementation-details.md)
