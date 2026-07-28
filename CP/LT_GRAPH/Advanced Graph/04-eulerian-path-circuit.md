# Eulerian Path And Circuit

Eulerian traversal uses every edge exactly once.

## Undirected Graph Rules

Eulerian circuit:

```text
all non-isolated nodes connected
every node has even degree
```

Eulerian path:

```text
all non-isolated nodes connected
exactly 0 or 2 nodes have odd degree
```

## Directed Graph Rules

Eulerian circuit:

```text
in[v] == out[v] for every node
all active nodes are in one connected component ignoring directions
```

Eulerian path from `s` to `t`:

```text
out[s] = in[s] + 1
in[t] = out[t] + 1
all other nodes have in == out
```

## Hierholzer

```cpp
void dfs(int u) {
    while (!g[u].empty()) {
        int v = g[u].back();
        g[u].pop_back();
        dfs(v);
    }
    path.push_back(u);
}
```

Reverse `path` at the end.

For undirected graphs, each edge must be marked used because it appears in both adjacency lists.

## Practice Problems

- CSES - Mail Delivery
- CSES - Teleporters Path
- CSES - De Bruijn Sequence

