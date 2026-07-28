# Graph And Operation Construction

Graph construction asks you to output vertices, edges, or operations so that graph properties hold.

Operation construction asks you to output a legal sequence that transforms one state into another.

Both require the same discipline:

```text
prove legality at every step
```

## Graph Building Blocks

### Path

```text
1 - 2 - 3 - ... - n
```

Properties:

- connected;
- `n - 1` edges;
- two vertices of degree `1`, others degree `2`;
- simple distances are easy to control.

### Star

```text
1 connected to every other vertex
```

Properties:

- connected;
- `n - 1` edges;
- one high-degree center;
- diameter `2` for `n > 2`.

### Cycle

```text
1 - 2 - 3 - ... - n - 1
```

Properties:

- every vertex degree `2`;
- connected;
- useful when all vertices need symmetric degree.

### Complete Graph

Every pair has an edge.

Properties:

- maximum number of edges: `n * (n - 1) / 2`;
- every vertex degree `n - 1`;
- useful when you need dense connectivity.

### Complete Bipartite Graph

Split vertices into `A` and `B`, connect every `A` to every `B`.

Properties:

- no edges inside a part;
- all cycles are even;
- useful for bipartite constraints and parity separation.

## Degree Construction

For degree constraints:

1. check sum of degrees is even;
2. check every degree is between `0` and `n - 1`;
3. decide whether graph must be simple, connected, tree, or multigraph;
4. use a known structure or Havel-Hakimi style greedy if needed.

For trees:

```text
sum of degrees = 2 * (n - 1)
```

If this fails, no tree exists.

## Connectivity Construction

If the graph must be connected, start with a path or tree using `n - 1` edges, then add extra edges.

```text
for i = 1..n-1:
  add edge i i+1

add remaining edges that do not break constraints
```

This is useful when the required edge count is at least `n - 1`.

## Operation Construction

Operations must be legal in the order printed. A valid final state is not enough.

Common strategies:

- normalize the object, then transform normalized form to target;
- build from left to right while never touching fixed positions again;
- use a buffer position;
- reverse destructive operations;
- record operations during simulation and print them at the end.

## Reverse Operations

If an operation removes information, reverse the process.

Examples:

- merging components forward becomes splitting components backward;
- deleting elements forward becomes adding elements backward;
- reducing values forward becomes increasing values backward.

Template:

```cpp
vector<Operation> ops;

while (!isBaseState(state)) {
    Operation op = chooseReverseOperation(state);
    applyReverse(state, op);
    ops.push_back(op);
}

reverse(ops.begin(), ops.end());
print(ops);
```

## Proving Operation Sequences

For each operation sequence, prove:

1. the chosen operation is legal at that moment;
2. the operation makes progress;
3. the process terminates within the operation limit;
4. the final state satisfies the target;
5. reversing operations, if used, preserves legality in the printed order.

## Common Bugs

- graph has duplicate edges;
- self-loops appear accidentally;
- edge count is off by one;
- graph is connected in examples but not in general;
- operation is legal in the final state but illegal when printed;
- operation count exceeds the limit.

## Practice Themes

- construct a tree with required degrees;
- construct connected graph with exact edge count;
- output swaps to transform one permutation into another;
- reverse deletion/merge operations;
- build graph satisfying parity or bipartite constraints.
