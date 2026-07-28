# Persistent Segment Tree

Persistent segment tree keeps old versions after updates.

## Use When

Use persistence when:

- queries refer to historical versions;
- every update creates a new array version;
- need kth/order/count query over prefixes;
- copying full arrays is too slow.

## Idea

Only nodes on the update path change. Reuse all other nodes.

```text
old root -> old nodes
new root -> new path + shared unchanged nodes
```

Each point update creates `O(log n)` new nodes.

## Node

```cpp
struct Node {
    int left = 0, right = 0;
    long long sum = 0;
};

vector<Node> seg(1);
```

## Versioned Roots

```text
root[0] = initial version
root[i] = version after i-th update
```

Query uses the root of the required version.

## Kth Number With Prefix Roots

Build prefix frequency versions:

```text
root[i] = root[i - 1] + one occurrence of a[i]
```

For range `[l, r]`, compare:

```text
root[r] - root[l - 1]
```

This counts frequencies only inside the range.

## Practice Problems

- CSES - Range Queries and Copies
- CSES - Range Interval Queries
- SPOJ - MKTHNUM

