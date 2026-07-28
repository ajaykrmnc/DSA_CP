# Suffix Array

Suffix array stores all suffixes of a string in sorted order.

## When To Use

Use suffix array for:

- distinct substring count;
- kth substring;
- repeated substring;
- substring order;
- lexicographic suffix queries.

## Doubling Idea

Sort suffixes by:

```text
first 2^k characters
```

At each step, combine two ranks:

```text
(rank[i], rank[i + 2^k])
```

## LCP Array

`lcp[i]` is the longest common prefix of adjacent suffixes:

```text
suffix_array[i] and suffix_array[i - 1]
```

Kasai computes it in `O(n)`.

```cpp
vector<int> buildLCP(const string& s, const vector<int>& sa) {
    int n = s.size();
    vector<int> rank(n), lcp(n);
    for (int i = 0; i < n; i++) rank[sa[i]] = i;

    int k = 0;
    for (int i = 0; i < n; i++) {
        if (rank[i] == 0) {
            k = 0;
            continue;
        }
        int j = sa[rank[i] - 1];
        while (i + k < n && j + k < n && s[i + k] == s[j + k]) k++;
        lcp[rank[i]] = k;
        if (k) k--;
    }
    return lcp;
}
```

## Distinct Substrings

Total substrings:

```text
n * (n + 1) / 2
```

Repeated prefixes counted by LCP:

```text
distinct = total - sum(lcp)
```

## Practice Problems

- CSES - Distinct Substrings
- CSES - Repeating Substring
- CSES - Substring Order I
- CSES - Substring Order II
- CSES - Substring Distribution
- CSES - Inverse Suffix Array

