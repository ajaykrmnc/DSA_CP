# Flow And Matching

Flow models movement of units through edges with capacities.

## Max Flow

Use max flow when:

- capacity limits exist;
- need maximum number of disjoint routes;
- need bipartite matching;
- min cut is required.

## Dinic Structure

Dinic repeats:

1. BFS builds levels.
2. DFS sends blocking flow along increasing levels.

Core edge:

```cpp
struct Edge {
    int to, rev;
    long long cap;
};
```

Residual edge lets flow be cancelled:

```text
forward cap decreases
reverse cap increases
```

## Bipartite Matching As Flow

Build:

```text
source -> left nodes capacity 1
left -> right edges capacity 1
right nodes -> sink capacity 1
```

Max flow equals maximum matching.

## Min Cut

After max flow, run DFS/BFS from source in residual graph using edges with positive capacity.

Cut edges are original edges:

```text
reachable[u] == true
reachable[v] == false
```

## Practice Problems

- CSES - Download Speed
- CSES - Police Chase
- CSES - School Dance
- CSES - Distinct Routes

