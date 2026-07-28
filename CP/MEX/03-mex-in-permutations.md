# MEX In Permutations

## Problem Statement

Use this when the statement asks for mex of prefixes, subarrays, or ranges of a permutation, especially with values `0..x` becoming interval constraints.

## Code

```cpp
vector<int> pos(n);
for (int i = 0; i < n; i++) {
    pos[p[i]] = i;
}
```

## Similar Problems

- Codeforces - prefix MEX permutation problems
- Codeforces - subarray MEX in permutation problems
- MEX construction problems where value positions matter
