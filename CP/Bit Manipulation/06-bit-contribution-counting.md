# Bit Contribution Counting

## Problem Statement

Use this when the answer is a sum over all pairs or all subarrays involving XOR, AND, or OR.

Instead of processing whole numbers, count contribution of each bit independently.

## Pair XOR Sum

Given array `a`, compute:

```text
sum over all i < j of (a[i] ^ a[j])
```

For bit `b`, a pair contributes `2^b` exactly when one value has bit `b` set and the other does not.

## Example

```text
a = [1, 2, 3]
binary: 01, 10, 11

bit 0: ones = 2, zeros = 1, contribution = 2 * 1 * 1
bit 1: ones = 2, zeros = 1, contribution = 2 * 1 * 2
answer = 6
```

## Code

```cpp
long long ans = 0;
for (int b = 0; b < 60; b++) {
    long long ones = 0;
    for (long long x : a) {
        if (x & (1LL << b)) ones++;
    }
    long long zeros = n - ones;
    ans += ones * zeros * (1LL << b);
}
```

## Pair AND Sum

A bit contributes only if both numbers have that bit.

```cpp
long long ans = 0;
for (int b = 0; b < 60; b++) {
    long long ones = 0;
    for (long long x : a) {
        if (x & (1LL << b)) ones++;
    }
    ans += ones * (ones - 1) / 2 * (1LL << b);
}
```

## Pair OR Sum

A bit contributes unless both numbers have `0`.

```cpp
long long ans = 0;
for (int b = 0; b < 60; b++) {
    long long ones = 0;
    for (long long x : a) {
        if (x & (1LL << b)) ones++;
    }
    long long zeros = n - ones;
    long long pairs = 1LL * n * (n - 1) / 2;
    ans += (pairs - zeros * (zeros - 1) / 2) * (1LL << b);
}
```

## Subarray XOR Sum

For each bit, count prefix parities. A subarray has bit `b` set when prefix parity changes.

```cpp
long long ans = 0;
for (int b = 0; b < 60; b++) {
    long long cnt[2] = {1, 0};
    int parity = 0;
    for (long long x : a) {
        parity ^= (x >> b) & 1;
        ans += cnt[parity ^ 1] * (1LL << b);
        cnt[parity]++;
    }
}
```

## Similar Problems

- Sum of pair XOR
- Sum of pair AND/OR
- Sum of subarray XOR
- Contribution-counting Codeforces problems
