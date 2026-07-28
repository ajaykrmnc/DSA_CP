# SOS DP

## Problem Statement

Given `freq[mask]`, compute information over all submasks or all supermasks for every mask.

Most common form:

```text
dp[mask] = sum of freq[sub] for every sub where sub is a submask of mask
```

Naive iteration over every `mask` and every `submask` is `O(3^n)`. SOS DP solves all masks in `O(n * 2^n)`.

## Example

```text
n = 3
mask = 101
submasks are 101, 100, 001, 000

dp[101] = freq[101] + freq[100] + freq[001] + freq[000]
```

## Subset Sum Code

```cpp
vector<long long> dp = freq;
for (int b = 0; b < n; b++) {
    for (int mask = 0; mask < (1 << n); mask++) {
        if (mask & (1 << b)) {
            dp[mask] += dp[mask ^ (1 << b)];
        }
    }
}
```

## Superset Sum Code

```cpp
vector<long long> dp = freq;
for (int b = 0; b < n; b++) {
    for (int mask = 0; mask < (1 << n); mask++) {
        if (!(mask & (1 << b))) {
            dp[mask] += dp[mask | (1 << b)];
        }
    }
}
```

## Count Compatible Masks

Problem: for each `mask`, count array masks `x` such that `(x & mask) == 0`.

```cpp
vector<int> dp = freq;
for (int b = 0; b < n; b++) {
    for (int mask = 0; mask < (1 << n); mask++) {
        if (mask & (1 << b)) dp[mask] += dp[mask ^ (1 << b)];
    }
}

int full = (1 << n) - 1;
for (int mask = 0; mask < (1 << n); mask++) {
    int compatible = dp[full ^ mask];
}
```

## Similar Problems

- Count pairs with `(a[i] & a[j]) == 0`
- Count masks that are subset/superset of query mask
- Codeforces subset DP problems
