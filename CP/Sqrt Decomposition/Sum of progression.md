# Sum of Progression

Problem: Codeforces 1921F - Sum of Progression

Each query gives `s, d, k` and asks for:

```text
a[s] + 2*a[s+d] + 3*a[s+2d] + ... + k*a[s+(k-1)d]
```

The positions are 1-indexed in the statement. Convert to 0-indexed in code.

## Key Idea

Split by `d`.

- If `d` is large, then the query visits at most `n / d` elements. Direct iteration is cheap.
- If `d` is small, precompute prefix sums along every residue class modulo `d`.

For each small `d`, build temporarily:

```text
sum[d][i] = a[i] + a[i-d] + a[i-2d] + ...
wsum[d][i] = (i/d + 1)*a[i] + (i/d)*a[i-d] + ...
```

For a query starting at `s` and ending at `r = s + (k - 1)*d`:

```text
plain = sum of a[s], a[s+d], ..., a[r]
weightedByPosition = sum of (pos/d + 1) * a[pos]

answer = weightedByPosition - (s/d) * plain
```

Why subtract `s / d`?

For every visited position `pos = s + t*d`:

```text
pos / d + 1 = s / d + t + 1
t + 1 = (pos / d + 1) - s / d
```

## Complexity

Let `B = sqrt(n)`.

| Part | Complexity |
|---|---:|
| Precompute small `d` | `O(n * B)` |
| Query with `d <= B` | `O(1)` |
| Query with `d > B` | `O(k)`, and `k <= n / d <= B` |
| Memory | `O(n + q)` if queries are grouped by `d` |

## Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Query {
    int s, d, k;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int n, q;
        cin >> n >> q;

        vector<ll> a(n);
        for (ll &x : a) cin >> x;

        int B = (int)sqrt(n) + 1;
        vector<Query> queries(q);
        vector<ll> ans(q, 0);
        vector<vector<int>> byStep(B + 1);

        for (int id = 0; id < q; id++) {
            int s, d, k;
            cin >> s >> d >> k;
            --s;
            queries[id] = {s, d, k};

            if (d <= B) {
                byStep[d].push_back(id);
            } else {
                for (int t = 0, pos = s; t < k; t++, pos += d) {
                    ans[id] += 1LL * (t + 1) * a[pos];
                }
            }
        }

        vector<ll> pref(n), weighted(n);
        for (int d = 1; d <= B; d++) {
            if (byStep[d].empty()) continue;

            fill(pref.begin(), pref.end(), 0);
            fill(weighted.begin(), weighted.end(), 0);

            for (int i = 0; i < n; i++) {
                pref[i] = a[i];
                weighted[i] = 1LL * (i / d + 1) * a[i];

                if (i - d >= 0) {
                    pref[i] += pref[i - d];
                    weighted[i] += weighted[i - d];
                }
            }

            for (int id : byStep[d]) {
                auto [s, step, k] = queries[id];
                int r = s + (k - 1) * step;

                ll plain = pref[r];
                ll byPos = weighted[r];

                if (s - step >= 0) {
                    plain -= pref[s - step];
                    byPos -= weighted[s - step];
                }

                ans[id] = byPos - 1LL * (s / step) * plain;
            }
        }

        for (int id = 0; id < q; id++) {
            cout << ans[id] << ' ';
        }
        cout << '\n';
    }

    return 0;
}
```

## Notes

- Use `long long`; answers can exceed `int`.
- The precomputed table works because all positions in a query have the same remainder modulo `d`.
- Do not store all `d` tables permanently unless memory limits are generous. Grouping queries by `d` keeps only one table in memory.
