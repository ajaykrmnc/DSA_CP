# Range Bitwise Queries

## Problem Statement

Use this when queries ask for bitwise AND, OR, XOR, or constraints over ranges.

Common variations:

- range XOR with prefix XOR;
- range AND/OR with sparse table;
- count set bits in a range;
- find longest subarray where bitwise AND/OR satisfies a condition.

## Range XOR

XOR has inverse cancellation, so prefix XOR works.

```cpp
vector<long long> pref(n + 1);
for (int i = 0; i < n; i++) pref[i + 1] = pref[i] ^ a[i];

long long rangeXor(int l, int r) {
    return pref[r + 1] ^ pref[l];
}
```

## Range AND Sparse Table

AND is idempotent:

```text
x & x = x
```

So sparse table can answer range AND in `O(1)`.

```cpp
vector<vector<int>> st(LOG, vector<int>(n));
st[0] = a;

for (int k = 1; k < LOG; k++) {
    for (int i = 0; i + (1 << k) <= n; i++) {
        st[k][i] = st[k - 1][i] & st[k - 1][i + (1 << (k - 1))];
    }
}

int rangeAnd(int l, int r) {
    int len = r - l + 1;
    int k = __lg(len);
    return st[k][l] & st[k][r - (1 << k) + 1];
}
```

## Range OR Sparse Table

The same structure works for OR:

```cpp
int rangeOr(int l, int r) {
    int len = r - l + 1;
    int k = __lg(len);
    return st[k][l] | st[k][r - (1 << k) + 1];
}
```

Build the table with `|` instead of `&`.

## Count Set Bits In Range

Precompute per-bit prefix counts.

```cpp
vector<vector<int>> pref(31, vector<int>(n + 1));
for (int b = 0; b < 31; b++) {
    for (int i = 0; i < n; i++) {
        pref[b][i + 1] = pref[b][i] + ((a[i] >> b) & 1);
    }
}

int countBit(int l, int r, int b) {
    return pref[b][r + 1] - pref[b][l];
}
```

## Monotonic Range AND

When extending a subarray to the right:

```text
AND can only lose bits.
OR can only gain bits.
```

This often allows binary search or two pointers if the target predicate is monotonic.

## Similar Problems

- Range XOR queries
- Range AND/OR queries
- Longest subarray with AND at least `k`
- Longest subarray with OR at least `k`
