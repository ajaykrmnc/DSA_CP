# DSU On Tree Small To Large

DSU on tree answers subtree queries by keeping data from the heavy child and merging light children into it.

## Use When

Use DSU on tree when:

- each query is about a subtree;
- node values/colors matter;
- naive merging maps for every node is too slow;
- small-to-large merging can reduce complexity.

## Small-To-Large Rule

When merging containers:

```text
always merge smaller container into larger container
```

Each element moves `O(log n)` times or less.

## DSU On Tree Idea

1. DFS to find heavy child by subtree size.
2. Solve light children and discard their data.
3. Solve heavy child and keep its data.
4. Add light children data into heavy data.
5. Answer query for current node.

## Practice Problems

- CSES - Distinct Colors
- Codeforces - Lomsat gelral

