# Integers Have Friends

Problem: Codeforces - Integers Have Friends

A subarray is valid if there exists an integer `m >= 2` such that every element has the same remainder modulo `m`.

For a subarray `a[l..r]`, this is equivalent to:

```text
a[l] == a[l+1] == ... == a[r] (mod m)
```

So every adjacent difference must be divisible by `m`:

```text
m divides |a[l+1] - a[l]|
m divides |a[l+2] - a[l+1]|
...
m divides |a[r] - a[r-1]|
```

Therefore the subarray is valid iff:

```text
gcd(|a[l+1]-a[l]|, |a[l+2]-a[l+1]|, ..., |a[r]-a[r-1]|) != 1
```

The gcd can be `0` only when all adjacent differences are `0`; that case is valid because all values are equal.

Length `1` is always valid because any `m >= 2` works.

## Key Idea

Build an array of adjacent differences:

```text
diff[i] = abs(a[i] - a[i - 1]) for i = 1..n-1
```

Then the original subarray `a[l..r]` maps to `diff[l+1..r]` in 1-indexed terms, or `diff[l..r-1]` in 0-indexed terms.

Now find the longest interval in `diff` whose gcd is not `1`. If that interval has length `x`, the answer in `a` has length `x + 1`.

## Approach 1: Two Pointers With GCD Sparse Table

Because gcd only decreases or stays the same when an interval expands, if `gcd(l, r) == 1`, then expanding `r` will not make the same left endpoint valid again. This gives a clean sliding window with range-gcd queries.

Complexity: `O(n log n)` per test case.

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct GcdSparseTable {
    int n;
    vector<int> lg;
    vector<vector<ll>> st;

    GcdSparseTable() {}

    GcdSparseTable(const vector<ll>& a) {
        n = (int)a.size();
        lg.assign(n + 1, 0);
        for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;

        int K = n == 0 ? 1 : lg[n] + 1;
        st.assign(K, vector<ll>(n, 0));
        if (n == 0) return;

        st[0] = a;
        for (int k = 1; k < K; k++) {
            for (int i = 0; i + (1 << k) <= n; i++) {
                st[k][i] = gcd(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
            }
        }
    }

    ll query(int l, int r) const {
        if (l > r) return 0;
        int k = lg[r - l + 1];
        return gcd(st[k][l], st[k][r - (1 << k) + 1]);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int n;
        cin >> n;

        vector<ll> a(n);
        for (ll &x : a) cin >> x;

        if (n == 1) {
            cout << 1 << '\n';
            continue;
        }

        vector<ll> diff(n - 1);
        for (int i = 1; i < n; i++) {
            diff[i - 1] = llabs(a[i] - a[i - 1]);
        }

        GcdSparseTable rmq(diff);

        int ans = 1;
        int l = 0;
        for (int r = 0; r < n - 1; r++) {
            while (l <= r && rmq.query(l, r) == 1) {
                l++;
            }
            if (l <= r) {
                ans = max(ans, r - l + 2);
            }
        }

        cout << ans << '\n';
    }

    return 0;
}
```

## Approach 2: Binary Search On Length

You can also binary search the answer length. For a candidate original length `len`, check whether any interval of `diff` with length `len - 1` has gcd not equal to `1`.

Complexity: `O(n log n)` after sparse table build.

This is often easier to reason about, but the two-pointer version is shorter once the monotonic gcd property is clear.

## Notes

- Use absolute differences; gcd should be non-negative.
- `gcd(0, x) = x`, and an all-equal segment has gcd `0`. Such a segment is valid because any `m >= 2` gives equal remainders.
- Invalid intervals are exactly those with gcd `1`; treat gcd `0` as valid.
