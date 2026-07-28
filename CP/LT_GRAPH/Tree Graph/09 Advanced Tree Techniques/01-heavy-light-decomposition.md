# Heavy-Light Decomposition

HLD breaks root-to-node paths into `O(log n)` heavy chains.

## Use When

Use HLD for:

- path query `u-v`;
- path update `u-v`;
- queries mixed with updates;
- operation can be handled by segment tree over chains.

## Idea

For each node:

```text
heavy child = child with largest subtree
```

Any root-to-node path crosses at most `O(log n)` light edges.

## Arrays

```text
parent[u]
depth[u]
heavy[u]
head[u] = top node of current chain
pos[u] = index in segment tree base array
```

## Path Query

```cpp
long long queryPath(int a, int b) {
    long long ans = 0;
    while (head[a] != head[b]) {
        if (depth[head[a]] < depth[head[b]]) swap(a, b);
        ans += seg.query(pos[head[a]], pos[a]);
        a = parent[head[a]];
    }
    if (depth[a] > depth[b]) swap(a, b);
    ans += seg.query(pos[a], pos[b]);
    return ans;
}
```

Change `+` to the required merge operation.

## Practice Problems

- CSES - Path Queries II
- CSES - Path Queries

