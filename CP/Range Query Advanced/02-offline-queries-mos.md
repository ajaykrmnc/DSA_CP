# Offline Queries And Mo's Algorithm

Offline queries can be reordered because all queries are known before answering.

## Offline Sorting

Common trick:

```text
sort events/queries by one endpoint
update data structure as pointer moves
answer each query when ready
```

Example: distinct values in `[l, r]`.

Process by increasing `r`. Track last occurrence of each value. Fenwick stores `1` only at the latest occurrence.

## Mo's Algorithm

Use Mo's algorithm when:

- array is static;
- queries are offline;
- adding/removing one element can update answer quickly;
- many arbitrary `[l, r]` queries exist.

Sort by block of `l`, then by `r`.

```cpp
int block = sqrt(n);
sort(q.begin(), q.end(), [&](Query a, Query b) {
    int ba = a.l / block;
    int bb = b.l / block;
    if (ba != bb) return ba < bb;
    return (ba & 1) ? a.r > b.r : a.r < b.r;
});
```

Maintain current range:

```text
while curL > L: add(--curL)
while curR < R: add(++curR)
while curL < L: remove(curL++)
while curR > R: remove(curR--)
```

## Practice Problems

- CSES - Distinct Values Queries
- CSES - Distinct Values Queries II
- Codeforces - Powerful Array

