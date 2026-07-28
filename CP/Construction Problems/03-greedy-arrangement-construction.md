# Greedy Arrangement Construction

Greedy construction works when you can safely place one part of the answer and leave the rest as the same kind of
problem.

The most common greedy rule is:

```text
place the hardest item first
```

Hardest can mean largest value, rarest character, most constrained position, highest degree, or a boundary cell.

## When Greedy Is Likely

Try greedy when:

- the statement asks for any valid arrangement;
- local conflicts are caused by adjacent or nearby elements;
- larger values are harder to fit than smaller values;
- positions have different numbers of allowed values;
- the problem has a natural left-to-right or outside-to-inside order.

## Greedy Patterns

### Largest First

Use this when values contribute to a sum or capacity.

Example:

```text
Need subset sum target T from numbers 1..n.
For x from n down to 1:
if x <= T:
take x
T -= x
```

This works for many `1..n` sum constructions because all smaller values remain available to fix the remainder.

### Most Constrained First

Sort tasks, positions, or vertices by constraint strength.

Examples:

- fill cells with fewer legal values first;
- assign high-degree graph vertices first;
- place rare characters first in a string;
- satisfy exact required positions before flexible positions.

### Alternating Extremes

To avoid equal or close neighbors:

```text
smallest, largest, second-smallest, second-largest, ...
```

or:

```text
largest, smallest, second-largest, second-smallest, ...
```

Use this for:

- avoiding adjacent differences below a threshold;
- creating many peaks and valleys;
- controlling local maxima/minima.

### Fill By Blocks

If a block of length `k` is valid and independent, repeat it.

Example:

```text
For binary string constraints:
0011 0011 0011 ...
```

Block construction is especially useful when constraints only look at windows of fixed length.

## Exchange Argument

To prove greedy, use an exchange argument:

```text
Assume an optimal/valid answer places smaller item before larger item.
Swap them.
The constraints do not get worse.
So there exists a valid answer following the greedy order.
```

For constructive problems, the proof does not need to show optimality. It only needs to show that the greedy choice
never destroys all possible completions.

## Common Failure Modes

1. Greedy satisfies local constraints but breaks a global sum.
2. Greedy works for large `n` but fails for small `n`.
3. Greedy assumes a remaining value exists without proving it.
4. Greedy prints duplicate values in a permutation.
5. Greedy uses a value outside the allowed range.

## Implementation Template

```cpp
vector<int> ans;
vector<int> used(n + 1, 0);

for (int step = 0; step < n; step++) {
  int chosen = -1;

  for (int x = 1; x <= n; x++) {
    if (used[x]) continue;
    if (canPlace(ans, x)) {
      chosen = x;
      break;
    }
  }

  if (chosen == -1) {
    cout << "NO\n";
    return;
  }

  used[chosen] = 1;
  ans.push_back(chosen);
}

cout << "YES\n";
for (int x : ans) cout << x << ' ';
cout << '\n';
```

For large constraints, replace the inner scan with a set, priority queue, or formula.

## Practice Themes

- equal-sum partition;
- rearrange string with no equal adjacent characters;
- permutation with no adjacent difference `1`;
- assigning numbers to satisfy prefix constraints;
- grid filling by rows, columns, or diagonals.
