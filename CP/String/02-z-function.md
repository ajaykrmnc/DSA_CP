# Z-Function

`z[i]` is the length of the longest substring starting at `i` that matches the prefix of the string.

## Template

```cpp
vector<int> zFunction(const string& s) {
    int n = s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i <= r) z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}
```

## Pattern Matching

Use:

```text
pattern + '#' + text
```

Any `z[i] >= pattern.size()` is a match.

## Finding Periods

A length `p` is a period if every position matches the character `p` before it.

With Z-function:

```text
if z[p] >= n - p, then p is a period
```

## KMP vs Z

Both solve many of the same problems.

- KMP prefix function is natural for borders.
- Z-function is natural for prefix matches from every position.

## Practice Problems

- CSES - String Matching
- CSES - Finding Periods
- CSES - String Functions

