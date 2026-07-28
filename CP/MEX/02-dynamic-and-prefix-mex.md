# Dynamic And Prefix MEX

## Problem Statement

Use this when the statement asks for mex after updates, mex of a moving range/window, prefix mex values, or many range/subtree mex queries.

## Code

```cpp
struct Mex {
    vector<int> freq;
    set<int> missing;

    Mex(int n) {
        freq.assign(n + 2, 0);
        for (int x = 0; x <= n + 1; x++) missing.insert(x);
    }

    void add(int x) {
        if (x < 0 || x >= (int)freq.size()) return;
        if (freq[x] == 0) missing.erase(x);
        freq[x]++;
    }

    void remove(int x) {
        if (x < 0 || x >= (int)freq.size()) return;
        freq[x]--;
        if (freq[x] == 0) missing.insert(x);
    }

    int get() const {
        return *missing.begin();
    }
};
```

```cpp
vector<int> prefixMex(const vector<int>& a) {
    int n = a.size();
    vector<int> seen(n + 2, 0), pref(n);
    int cur = 0;

    for (int i = 0; i < n; i++) {
        if (0 <= a[i] && a[i] <= n) seen[a[i]] = 1;
        while (seen[cur]) cur++;
        pref[i] = cur;
    }

    return pref;
}
```

```cpp
struct MexBuckets {
    int n, B;
    vector<int> freq, zeroCount;

    MexBuckets(int n_) : n(n_), B(450), freq(n_ + 2, 0) {
        int blocks = (n + B + 1) / B;
        zeroCount.assign(blocks, 0);
        for (int x = 0; x <= n + 1; x++) zeroCount[x / B]++;
    }

    void add(int x) {
        if (x < 0 || x > n + 1) return;
        if (freq[x] == 0) zeroCount[x / B]--;
        freq[x]++;
    }

    void remove(int x) {
        if (x < 0 || x > n + 1) return;
        freq[x]--;
        if (freq[x] == 0) zeroCount[x / B]++;
    }

    int get() {
        for (int b = 0; b < (int)zeroCount.size(); b++) {
            if (zeroCount[b] == 0) continue;
            int start = b * B;
            int end = min(n + 1, start + B - 1);
            for (int x = start; x <= end; x++) {
                if (freq[x] == 0) return x;
            }
        }
        return n + 1;
    }
};
```

## Similar Problems

- Codeforces - MEX Queries
- Codeforces - sliding window MEX problems
- Tree/subtree mex problems with small-to-large merging
