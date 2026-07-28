# MEX Basics

## Problem Statement

Use this when the statement asks for the smallest missing non-negative value, asks you to construct an array with a target mex, or gives direct mex constraints.

## Code

```cpp
int mexVector(const vector<int>& a) {
    int n = a.size();
    vector<int> seen(n + 2, 0);

    for (int x : a) {
        if (0 <= x && x <= n) seen[x] = 1;
    }

    for (int x = 0; x <= n + 1; x++) {
        if (!seen[x]) return x;
    }
    return n + 1;
}
```

## Similar Problems

- LeetCode 41 - First Missing Positive
- CSES - Mex Grid Construction
- Codeforces - basic MEX construction problems
