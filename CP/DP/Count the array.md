# Count tdsfhe array

**Problem Statement:**
Given an array of integers, find the minimum number of subarrays needed to partition the array such that each subarray
can be reduced to a single element by repeatedly merging adjacent equal elements. When two adjacent elements are equal,
they can be merged into a single element with value increased by 1.

This is an interval dynamic programming problem where you need to find the optimal way to partition the array. Use DP to
compute for each subarray [i,j] the final value it can be reduced to, then use another DP to find the minimum partitions
needed.

```cpp
#include <bits/stdc++.h>
using namespace std;

const int N = 505;

int a[N];
int f[N][N];
int dp[N];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;

  for (int i = 1; i <= n; i++) {
    cin >> a[i];
    f[i][i] = a[i];
  }

  for (int len = 2; len <= n; len++) {
    for (int l = 1; l + len - 1 <= n; l++) {
      int r = l + len - 1;
      for (int j = l; j < r; j++) {
        if (f[l][j] && f[l][j] == f[j + 1][r])
          f[l][r] = f[l][j] + 1;
      }
    }
  }

  for (int i = 1; i <= n; i++) {
    dp[i] = 1e7;
    for (int j = 0; j < i; j++)
      if (f[j + 1][i]) dp[i] = min(dp[i], dp[j] + 1);
  }

  cout << dp[n] << endl;
}
```

[Some Interval DP Problems and State Reduction - Codeforces](https://codeforces.com.cn/blog/entry/108850)

