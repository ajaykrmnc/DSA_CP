# Functional Graphs

A functional graph is a directed graph where every node has exactly one outgoing edge.

Each component contains:

```text
one directed cycle
with trees feeding into that cycle
```

## Use When

Use this pattern when:

- every node points to exactly one next node;
- repeated jumps are needed;
- the problem asks where you land after `k` steps;
- cycle length or distance to cycle is needed.

## Binary Lifting For K Jumps

```cpp
const int LOG = 60;
vector<array<int, LOG>> up(n);

for (int v = 0; v < n; v++) up[v][0] = nxt[v];

for (int j = 1; j < LOG; j++) {
    for (int v = 0; v < n; v++) {
        up[v][j] = up[up[v][j - 1]][j - 1];
    }
}

int jump(int v, long long k) {
    for (int j = 0; j < LOG; j++) {
        if (k & (1LL << j)) v = up[v][j];
    }
    return v;
}
```

## Cycle Detection

Use DFS colors:

```text
0 = unvisited
1 = currently in stack
2 = done
```

When DFS reaches a color `1` node, a cycle is found.

## Practice Problems

- CSES - Planets Queries I
- CSES - Planets Queries II
- CSES - Planets Cycles

