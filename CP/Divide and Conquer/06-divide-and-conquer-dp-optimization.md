# Divide And Conquer DP Optimization

## Problem Statement

Use this when a DP transition has one split point `k`, the previous DP layer is already computed, `cost(l, r)` is fast
enough, and the optimal split index is monotonic.

## Code

```cpp
const long long INF = 4e18;
vector<vector<long long>> dp;

long long cost(int l, int r);

void compute(int g, int l, int r, int optL, int optR) {
  if (l > r) return;

  int mid = l + (r - l) / 2;
  pair<long long, int> best = {INF, -1};

  int upper = min(mid, optR);
  for (int k = optL; k <= upper; k++) {
    long long val = dp[g - 1][k] + cost(k + 1, mid);
    if (val < best.first) {
      best = {val, k};
    }
  }

  dp[g][mid] = best.first;
  int opt = best.second;

  compute(g, l, mid - 1, optL, opt);
  compute(g, mid + 1, r, opt, optR);
}
```

## Similar Problems

- Divide array into groups with interval cost
- DP partition optimization problems with monotonic opt
- Range-cost grouping DP problems
