# Parity Masks And Bitsets

## Problem Statement

Use parity masks when only odd/even frequency matters. Use bitsets when many boolean values must be combined quickly.

Common variations:

- count substrings that can be rearranged into a palindrome;
- compare rows/strings by Hamming distance;
- count grid pairs sharing columns;
- speed up boolean DP or graph reachability.

## Parity Mask Example

```text
s = "aba"

a toggles bit 0
b toggles bit 1
a toggles bit 0 again

final mask has only bit 1 set, so at most one odd count exists.
```

A multiset can be rearranged into a palindrome if:

```text
mask == 0 or mask has exactly one set bit
```

## Parity Code

```cpp
int mask = 0;
for (char c : s) {
    mask ^= 1 << (c - 'a');
}

bool ok = mask == 0 || (mask & (mask - 1)) == 0;
```

## Count Wonderful Substrings

Problem: count substrings where at most one character has odd frequency.

```cpp
long long ans = 0;
vector<long long> cnt(1 << 10);
int mask = 0;
cnt[0] = 1;

for (char c : s) {
    mask ^= 1 << (c - 'a');
    ans += cnt[mask];
    for (int b = 0; b < 10; b++) {
        ans += cnt[mask ^ (1 << b)];
    }
    cnt[mask]++;
}
```

## Bitset Example

Given binary grid rows, count how many pairs of rows have common `1` columns.

```cpp
bitset<MAXN> row[MAXN];

long long ans = 0;
for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
        int common = (row[i] & row[j]).count();
        ans += 1LL * common * (common - 1) / 2;
    }
}
```

## Hamming Distance

```cpp
bitset<MAXN> a, b;
int dist = (a ^ b).count();
```

## Similar Problems

- CSES - Hamming Distance
- CSES - Beautiful Subgrids
- LeetCode 1915 - Number of Wonderful Substrings
- Palindrome permutation substring problems
