# Sparse Table

Sparse table answers static idempotent range queries in `O(1)` after `O(n log n)` preprocessing.

## Use When

Use sparse table when:

- array does not change;
- query operation is idempotent: `min`, `max`, `gcd`;
- many range queries exist.

Not good for:

- point/range updates;
- sum queries requiring overlapping intervals unless using disjoint decomposition in `O(log n)`.

## Build

```cpp
int K = 20;
vector<vector<int>> st(K, vector<int>(n));
st[0] = a;

for (int j = 1; j < K; j++) {
    for (int i = 0; i + (1 << j) <= n; i++) {
        st[j][i] = min(st[j - 1][i],
                       st[j - 1][i + (1 << (j - 1))]);
    }
}
```

## Query Minimum

```cpp
int queryMin(int l, int r) {
    int len = r - l + 1;
    int j = 31 - __builtin_clz(len);
    return min(st[j][l], st[j][r - (1 << j) + 1]);
}
```

## Practice Problems

- CSES - Static Range Minimum Queries
- CSES - Range Minimum Queries I

