# Permutation Construction Patterns

## Problem Statement

Use this when the statement asks you to print any permutation satisfying local, prefix, forbidden-position, distance, parity, or ordering constraints.

## Code

```cpp
set<int> unused;
for (int x = 1; x <= n; x++) unused.insert(x);

for (int idx : order) {
    auto it = unused.lower_bound(need[idx]);
    if (it == unused.end()) {
        // impossible
    }
    p[idx] = *it;
    unused.erase(it);
}
```

## Similar Problems

- CSES - Permutations
- Codeforces constructive permutation problems
- LeetCode 31 - Next Permutation
