# Core Bit Tricks

## Problem Statement

Use this when the problem asks about bits directly: count set bits, test powers of two, generate subsets, find the lowest
set bit, or move through binary representation.

## Example

```text
x = 12 = 1100
lowest set bit = 0100 = 4
x after removing lowest set bit = 1000 = 8
```

## Basic Code

```cpp
bool hasBit(long long x, int b) {
    return x & (1LL << b);
}

long long setBit(long long x, int b) {
    return x | (1LL << b);
}

long long clearBit(long long x, int b) {
    return x & ~(1LL << b);
}

long long toggleBit(long long x, int b) {
    return x ^ (1LL << b);
}
```

## Lowest Set Bit

```cpp
long long lowbit(long long x) {
    return x & -x;
}
```

## Count Set Bits

```cpp
int cnt = __builtin_popcountll(x);
```

Manual version:

```cpp
int cnt = 0;
while (x) {
    x &= x - 1;
    cnt++;
}
```

## Power Of Two

```cpp
bool isPowerOfTwo(long long x) {
    return x > 0 && (x & (x - 1)) == 0;
}
```

## Enumerate All Masks

```cpp
for (int mask = 0; mask < (1 << n); mask++) {
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) {
            // item i is selected
        }
    }
}
```

## Similar Problems

- CSES - Counting Bits
- LeetCode 191 - Number of 1 Bits
- LeetCode 231 - Power of Two
- Basic subset generation problems
