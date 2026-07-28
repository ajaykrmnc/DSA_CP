# Mask DP And Submask Iteration

## Problem Statement

Use mask DP when `n` is small and each element is either selected or not selected.

Typical constraints:

```text
n <= 20 for O(n * 2^n)
n <= 16 for O(n^2 * 2^n)
```

## Example State

```text
dp[mask] = best answer after selecting exactly the elements in mask
```

If `mask = 10110`, then elements `1`, `2`, and `4` are selected.

## Basic Transition

Problem: count ways to build a valid ordering.

```cpp
vector<long long> dp(1 << n);
dp[0] = 1;

for (int mask = 0; mask < (1 << n); mask++) {
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) continue;
        if (!canAdd(mask, i)) continue;
        dp[mask | (1 << i)] += dp[mask];
    }
}
```

## Assignment DP

Problem: assign each row to one unused column with minimum cost.

```cpp
const long long INF = 4e18;
vector<long long> dp(1 << n, INF);
dp[0] = 0;

for (int mask = 0; mask < (1 << n); mask++) {
    int row = __builtin_popcount(mask);
    for (int col = 0; col < n; col++) {
        if (mask & (1 << col)) continue;
        int nmask = mask | (1 << col);
        dp[nmask] = min(dp[nmask], dp[mask] + cost[row][col]);
    }
}
```

## Submask Iteration

Problem: split a set into two parts or process every subset of `mask`.

```cpp
for (int sub = mask; sub; sub = (sub - 1) & mask) {
    int other = mask ^ sub;
}
```

Include empty submask if needed:

```cpp
for (int sub = mask;; sub = (sub - 1) & mask) {
    // use sub
    if (sub == 0) break;
}
```

## Superset Iteration

Problem: process every mask that contains `mask`.

```cpp
int full = (1 << n) - 1;
for (int sup = mask; sup <= full; sup = (sup + 1) | mask) {
    // use sup
    if (sup == full) break;
}
```

## Complexity Note

All submasks over all masks:

```text
sum over masks of 2^popcount(mask) = 3^n
```

## Similar Problems

- CSES - Hamiltonian Flights
- CSES - Elevator Rides
- AtCoder DP O - Matching
- LeetCode 1879 - Minimum XOR Sum of Two Arrays
