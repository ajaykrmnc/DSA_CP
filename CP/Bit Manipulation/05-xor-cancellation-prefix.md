# XOR Cancellation And Prefix XOR

## Problem Statement

Use this when equal values cancel, when the statement asks for subarray XOR, or when each value appears an even number
of times except a few special values.

Key identities:

```text
x ^ x = 0
x ^ 0 = x
x ^ y = y ^ x
```

## Example 1: One Single Number

```text
a = [4, 1, 2, 1, 2]
answer = 4
```

```cpp
long long ans = 0;
for (long long x : a) ans ^= x;
```

## Example 2: Two Single Numbers

All numbers appear twice except two numbers `x` and `y`.

```text
a = [1, 2, 1, 3, 2, 5]
x ^ y = 3 ^ 5 = 6
Use one set bit of 6 to split numbers into two groups.
```

```cpp
long long all = 0;
for (long long x : a) all ^= x;

long long bit = all & -all;
long long x = 0, y = 0;
for (long long v : a) {
    if (v & bit) x ^= v;
    else y ^= v;
}
```

## Example 3: One Number Appears Once, Others Appear Three Times

XOR alone does not work when duplicates appear three times. Count each bit modulo `3`.

```text
a = [2, 2, 3, 2]
bit counts modulo 3 reconstruct 3.
```

```cpp
long long ans = 0;
for (int b = 0; b < 60; b++) {
    int cnt = 0;
    for (long long x : a) {
        cnt += (x >> b) & 1;
    }
    if (cnt % 3) ans |= 1LL << b;
}
```

## Prefix XOR

Problem: answer XOR of subarray `[l, r]`.

```text
pref[i] = a[0] ^ a[1] ^ ... ^ a[i - 1]
xor(l, r) = pref[r + 1] ^ pref[l]
```

```cpp
vector<long long> pref(n + 1);
for (int i = 0; i < n; i++) pref[i + 1] = pref[i] ^ a[i];

long long getXor(int l, int r) {
    return pref[r + 1] ^ pref[l];
}
```

## Count Subarrays With XOR K

```cpp
long long ans = 0;
unordered_map<long long, long long> cnt;
cnt[0] = 1;

long long pref = 0;
for (long long x : a) {
    pref ^= x;
    ans += cnt[pref ^ k];
    cnt[pref]++;
}
```

## Similar Problems

- LeetCode 136 - Single Number
- LeetCode 137 - Single Number II
- LeetCode 260 - Single Number III
- LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
- Subarray XOR equals `k`
