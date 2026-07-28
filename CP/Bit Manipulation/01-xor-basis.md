# XOR Basis

## Problem Statement

Given an array `a`, answer questions about XOR values obtainable by choosing any subset of elements.

Common variations:

- maximum possible subset XOR;
- check whether a value `x` can be formed;
- count distinct subset XOR values;
- maximum XOR path/cycle value in graphs.

## Example

```text
a = [3, 5, 6]

3 ^ 5 = 6, so 6 is dependent on 3 and 5.
Possible maximum subset XOR is 6.
```

## Idea

Treat every number as a binary vector. Keep one independent vector for each highest set bit.

If a new number can be reduced to `0`, it does not add a new XOR value.
If it cannot, store it as a new basis vector.

## Code

```cpp
const int LOG = 60;
long long basis[LOG];

void insertVector(long long x) {
    for (int b = LOG - 1; b >= 0; b--) {
        if (!(x & (1LL << b))) continue;
        if (!basis[b]) {
            basis[b] = x;
            return;
        }
        x ^= basis[b];
    }
}

long long maxXor() {
    long long ans = 0;
    for (int b = LOG - 1; b >= 0; b--) {
        ans = max(ans, ans ^ basis[b]);
    }
    return ans;
}
```

## Can Form X

```cpp
bool canForm(long long x) {
    for (int b = LOG - 1; b >= 0; b--) {
        if (x & (1LL << b)) x ^= basis[b];
    }
    return x == 0;
}
```

## Count Distinct XORs

If the rank of the basis is `r`, then the number of distinct subset XOR values is:

```text
2^r
```

## Similar Problems

- Maximum subset XOR
- Codeforces XOR basis problems
- Graph XOR path with cycles
