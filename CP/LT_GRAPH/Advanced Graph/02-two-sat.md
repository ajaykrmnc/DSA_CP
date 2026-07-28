# 2-SAT

2-SAT checks if boolean variables can satisfy clauses of size two.

Clause:

```text
(a OR b)
```

Implications:

```text
(!a -> b)
(!b -> a)
```

Build an implication graph and run SCC.

## Variable Encoding

For variable `x`:

```text
2*x     = false
2*x + 1 = true
```

Negation:

```cpp
int neg(int node) {
    return node ^ 1;
}
```

## Satisfiability Rule

For every variable `x`:

```text
if comp[2*x] == comp[2*x + 1], impossible
```

Assignment can be derived by reverse topological order of SCCs:

```text
value[x] = comp[true] > comp[false]
```

The comparison direction depends on SCC numbering order.

## Practice Problems

- CSES - Giant Pizza

