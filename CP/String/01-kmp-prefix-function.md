# KMP Prefix Function

KMP solves exact pattern matching in `O(n + m)`.

## Prefix Function

`pi[i]` is the length of the longest proper prefix of `s[0..i]` that is also a suffix of `s[0..i]`.

```cpp
vector<int> prefixFunction(const string& s) {
    int n = s.size();
    vector<int> pi(n);
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    return pi;
}
```

## Pattern Matching

Build:

```text
pattern + '#' + text
```

Every position where prefix value equals `pattern.size()` is a match.

## Borders

A border is a string that is both prefix and suffix.

After computing `pi`, all borders of `s` can be found by:

```cpp
for (int k = pi[n - 1]; k > 0; k = pi[k - 1]) {
    // k is a border length
}
```

## How To Identify

Use KMP when:

- exact substring matching is needed;
- borders or periods are needed;
- repeated prefix/suffix structure matters.

## Practice Problems

- CSES - String Matching
- CSES - Finding Borders
- CSES - Finding Periods
- CSES - Required Substring

