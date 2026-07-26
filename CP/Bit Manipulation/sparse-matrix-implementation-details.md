# Sparse Matrix / Sparse Table

**Problem Statement:**
Given an array of integers, answer many range queries efficiently. In bit manipulation problems, common range
queries include bitwise AND, OR, XOR, minimum, maximum, and GCD over a subarray.

A sparse matrix, more commonly called a sparse table in CP, stores precomputed answers for intervals whose
lengths are powers of two. The matrix cell `sp[i][j]` represents the answer for the range starting at index
`i` with length `2^j`.

For example:

```text
sp[i][0] = a[i]
sp[i][1] = operation(a[i], a[i + 1])
sp[i][2] = operation(a[i..i + 3])
sp[i][3] = operation(a[i..i + 7])
```

## When to Use

Use a sparse table when:

- The array is static.
- There are many range queries.
- The operation can combine two adjacent intervals.
- For `O(1)` queries, the operation should be idempotent, such as `min`, `max`, `gcd`, `AND`, or `OR`.

For non-idempotent operations like sum or XOR, sparse table can still be used, but range queries usually need
to decompose the query range into multiple power-of-two blocks, giving `O(log n)` per query.

## When Not to Use

Do not use a sparse table when:

- The array has frequent updates.
- You need range updates.
- Memory is tight and `O(n log n)` space is too large.
- The operation is not associative.
- You only have a few queries, where a simple loop is enough.
- The operation is non-idempotent and you specifically need `O(1)` range queries.

For update-heavy problems, prefer a segment tree or Fenwick tree depending on the operation.

## Quick Decision Table

| Requirement | Better Choice |
| --- | --- |
| Static array + range min/max/gcd/AND/OR | Sparse table |
| Static array + range XOR | Prefix XOR |
| Static array + range sum | Prefix sum |
| Point updates + range queries | Segment tree / Fenwick tree |
| Range updates + range queries | Lazy segment tree |
| Need only one or two queries | Direct loop |
| Need kth/order/statistical queries | Depends: merge sort tree, wavelet tree, PBDS, etc. |

## Build Formula

To build `sp[i][j]`, combine two intervals of length `2^(j - 1)`:

```cpp
sp[i][j] = merge(sp[i][j - 1], sp[i + (1 << (j - 1))][j - 1]);
```

This works because:

```text
[i, i + 2^j - 1]
= [i, i + 2^(j - 1) - 1] + [i + 2^(j - 1), i + 2^j - 1]
```

## Query Formula for Idempotent Operations

For operations like `min`, `max`, `gcd`, `AND`, and `OR`, answer `[l, r]` using two overlapping blocks of
length `2^k`, where `k = floor(log2(r - l + 1))`.

```cpp
answer = merge(sp[l][k], sp[r - (1 << k) + 1][k]);
```

The overlap is fine because idempotent operations satisfy:

```text
x op x = x
```

For bitwise AND:

```text
x & x = x
```

## Complexity

- Build time: `O(n log n)`
- Query time for idempotent operations: `O(1)`
- Query time for non-idempotent operations: `O(log n)`
- Space: `O(n log n)`

## Generic Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

struct SparseTable {
  int n, lg;
  vector<vector<int>> sp;
  vector<int> logVal;

  int mergeValue(int a, int b) {
    return a & b; // change this to min(a, b), max(a, b), gcd(a, b), a | b, etc.
  }

  SparseTable(const vector<int>& arr) {
    n = (int)arr.size();
    lg = 32 - __builtin_clz(n);

    sp.assign(n, vector<int>(lg));
    logVal.assign(n + 1, 0);

    for (int i = 2; i <= n; i++) {
      logVal[i] = logVal[i / 2] + 1;
    }

    for (int i = 0; i < n; i++) {
      sp[i][0] = arr[i];
    }

    for (int j = 1; j < lg; j++) {
      for (int i = 0; i + (1 << j) <= n; i++) {
        sp[i][j] = mergeValue(sp[i][j - 1], sp[i + (1 << (j - 1))][j - 1]);
      }
    }
  }

  int query(int l, int r) {
    int len = r - l + 1;
    int k = logVal[len];
    return mergeValue(sp[l][k], sp[r - (1 << k) + 1][k]);
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, q;
  cin >> n >> q;

  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  SparseTable st(a);

  while (q--) {
    int l, r;
    cin >> l >> r;
    --l;
    --r;

    cout << st.query(l, r) << '\n';
  }

  return 0;
}
```

## XOR Query Variant

XOR is associative, but it is not idempotent because `x ^ x = 0`, not `x`. So the two-block `O(1)` sparse
table query method does not work for XOR.

For static XOR range queries, prefix XOR is simpler and faster:

```cpp
vector<int> pref(n + 1, 0);

for (int i = 0; i < n; i++) {
  pref[i + 1] = pref[i] ^ a[i];
}

int rangeXor(int l, int r) {
  return pref[r + 1] ^ pref[l];
}
```

Use sparse table for XOR only when you specifically need to split ranges into power-of-two blocks for a more
complex algorithm.

## Important Details

- Use 0-based indexing internally to avoid off-by-one mistakes.
- Precompute logs instead of calling `log2` inside every query.
- Make sure `sp` has enough columns: `floor(log2(n)) + 1`.
- Bitwise AND over a growing range is monotonic non-increasing.
- Bitwise OR over a growing range is monotonic non-decreasing.
- These monotonic properties are useful when combining sparse table queries with binary search.
