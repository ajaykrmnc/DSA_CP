# SCC And Condensation DAG

Strongly connected components compress a directed graph into a DAG.

## Use When

Use SCC when:

- directed graph has cycles;
- nodes mutually reachable should behave as one component;
- after compression, DP/topological order becomes possible.

## Kosaraju

1. DFS on original graph and push nodes by exit time.
2. Reverse all edges.
3. Process nodes in reverse exit order on the reversed graph.

```cpp
void dfs1(int u, vector<vector<int>>& g, vector<int>& vis, vector<int>& order) {
    vis[u] = 1;
    for (int v : g[u]) if (!vis[v]) dfs1(v, g, vis, order);
    order.push_back(u);
}

void dfs2(int u, vector<vector<int>>& rg, vector<int>& comp, int id) {
    comp[u] = id;
    for (int v : rg[u]) if (comp[v] == -1) dfs2(v, rg, comp, id);
}
```

## Condensation DAG

After SCC:

```text
if comp[u] != comp[v], add edge comp[u] -> comp[v]
```

The condensation graph is always a DAG.

## Practice Problems

- CSES - Planets and Kingdoms
- CSES - Coin Collector
- CSES - Giant Pizza

