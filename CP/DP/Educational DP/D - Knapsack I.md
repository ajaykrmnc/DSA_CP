# D - Knapsack I

**Problem Statement:**
Given N items, each with a weight w[i] and value v[i], and a knapsack with capacity W, find the maximum value that can
be obtained by selecting items such that their total weight doesn't exceed W. This is the classic 0/1 knapsack problem
where each item can be either included or excluded. Use dynamic programming where dp[i][w] represents the maximum value
achievable using the first i items with weight limit w. The recurrence relation is: dp[i][w] = max(dp[i-1][w],
dp[i-1]w-weight[i]] + value[i]) if weight[i] <= w.

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 1000005;
[int](2026-07-17_int.md) vec[N][2];
int dp[101][100005];

int fun(int i, int m) {
  if (i < 0)
    return 0;
  if (dp[i][m] != -1)
    return dp[i][m];
  int w = vec[i][0];
  int v = vec[i][1];
  if (m - w < 0)
    return dp[i][m] = fun(i - 1, m);

  int maxi = max(v + fun(i - 1, m - w), fun(i - 1, m));

  return dp[i][m] = maxi;
}

int32_t main() {
  speed();
  memset(dp, -1, sizeof(dp));
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    cin >> vec[i][0] >> vec[i][1];
  }
  cout << fun(n - 1, m) << nline;

  return 0;
}

```

