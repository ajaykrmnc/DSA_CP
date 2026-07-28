# Impossibility Proofs

Constructive problems usually require both:

```text
NO proof: why impossible cases are impossible
YES proof: why your construction always works
```

Many wrong submissions only have a construction. If the construction fails, they print `NO` even though another
construction may exist.

## Types Of Impossibility

### Parity

If every operation changes a value by an even amount, parity cannot change.

```text
start parity != target parity -> impossible
```

### Sum

If operations move value without creating or deleting it, total sum is fixed.

```text
start sum != target sum -> impossible
```

If splitting into equal groups:

```text
total sum must be divisible by number of groups
```

### Bounds

Sometimes the target asks for more than the maximum possible or less than the minimum possible.

Examples:

- too many edges for a simple graph;
- degree greater than `n - 1`;
- sum too small or too large for fixed length;
- more distinct values than available.

### Pigeonhole Principle

If too many objects must fit into too few categories, some conflict is forced.

Example:

```text
Need n adjacent pairs all with different colors,
but only two colors exist and the graph forces an odd cycle.
```

### Coloring

Coloring gives impossibility for grids, graphs, and movement.

Examples:

- dominoes need equal black/white covered cells;
- knight/bishop/rook movement may preserve or flip color classes;
- bipartite graphs cannot contain odd cycles.

### Graph Degree

For simple graphs:

```text
0 <= degree[v] <= n - 1
sum(degree) must be even
```

For trees:

```text
edges = n - 1
sum(degree) = 2 * (n - 1)
connected + acyclic
```

### Small Cases

Some constructions are impossible only for tiny inputs.

Example:

```text
CSES Permutations:
n = 1 works
n = 2, 3 impossible
n >= 4 works
```

Small cases need explicit reasoning because general patterns often start at `n >= 4` or `n >= 5`.

## How To Avoid False `NO`

Before printing `NO`, ask:

1. Did I prove impossible by an invariant or bound?
2. Or did my current construction merely fail?
3. Is there another shape: reverse, parity split, cyclic shift, greedy, graph block?
4. Did I test small cases manually?

Only print `NO` when a required condition is violated or a complete case analysis proves failure.

## Proof Template

Use this structure in editorials and personal notes:

```text
Necessary condition:
Explain what every valid answer must satisfy.

Impossible case:
If condition fails, print NO.

Construction:
Describe the pattern.

Correctness:
Prove the object uses legal values.
Prove every required constraint.
Prove all cases are covered.

Complexity:
State time and memory.
```

## Example Proof: Evens Then Odds

Problem:

```text
Construct permutation 1..n such that adjacent difference is never 1.
```

Impossible:

- `n = 2`: only `1 2` or `2 1`, adjacent difference is `1`;
- `n = 3`: every permutation places two consecutive values adjacent.

Construction for `n >= 4`:

```text
2 4 6 ... 1 3 5 ...
```

Correctness:

- all values `1..n` appear once;
- adjacent values inside the even block differ by `2`;
- adjacent values inside the odd block differ by `2`;
- the boundary between the last even and first odd has difference greater than `1` for `n >= 4`.

## Practice Themes

- parity impossibility;
- equal-sum partition impossibility;
- grid coloring impossibility;
- graph degree impossibility;
- small-case constructive exceptions.
