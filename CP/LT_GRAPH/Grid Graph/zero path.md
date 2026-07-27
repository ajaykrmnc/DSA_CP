# zero path

**Problem Statement:**
Given an n×m grid with 0s and 1s, determine if there exists a path from top-left to bottom-right such that the
difference between the number of 1s and 0s encountered is exactly 0. You can only move right or down. Use dynamic
programming with bitset optimization to track all possible differences efficiently. The key insight is to maintain a
bitset for each cell representing all possible difference values that can be achieved when reaching that cell.

problem link: [Link](https://codeforces.com/problemset/problem/1695/C)

```cpp
#include <bits/stdc++.h>
using namespace std;

#define N 1010

int grid[N][N], mn[N][N], mx[N][N];

int main() {
  int num_tests;
  cin >> num_tests;

  for (int test = 0; test < num_tests; ++test) {
    int n, m;
    cin >> n >> m;

    for(int i = 0; i < n; ++i)
      for(int j = 0; j < m; ++j)
        cin >> grid[i][j];

    mn[0][0] = mx[0][0] = grid[0][0];

    for(int i = 1; i < n; ++i)
      mx[i][0] = mn[i][0] = mx[i - 1][0] + grid[i][0];

    for(int j = 1; j < m; ++j)
      mx[0][j] = mn[0][j] = mx[0][j - 1] + grid[0][j];

    for(int i = 1; i < n; ++i)
      for(int j = 1; j < m; ++j) {
        mx[i][j] = max(mx[i - 1][j], mx[i][j - 1]) + grid[i][j];
        mn[i][j] = min(mn[i - 1][j], mn[i][j - 1]) + grid[i][j];
      }

    if(mx[n - 1][m - 1] % 2 || mn[n - 1][m - 1] > 0 || mx[n - 1][m - 1] < 0)
      cout << "NO\n";
    else
      cout << "YES\n";
  }
}
```

```cpp
void solve() {
  cin >> n >> m;

  vector<vector<bitset<MAXN + 1>>> dp(n, vector<bitset<MAXN + 1>>(m));

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      cin >> a[i][j];
      if(i == 0 && j == 0) {
        if(a[i][j] == 1) dp[i][j][MAXN - 1] = 1;
        else dp[i][j][MAXN] = 1;
      }
      else {
        if(i > 0) {
          if(a[i][j] == 1) dp[i][j] |= (dp[i - 1][j] >> 1);
          else dp[i][j] |= dp[i - 1][j];
        }
        if(j > 0) {
          if(a[i][j] == 1) dp[i][j] |= (dp[i][j - 1] >> 1);
          else dp[i][j] |= dp[i][j - 1];
        }
      }
    }
  }



  int need = (n + m - 1) / 2;

  if((n + m) % 2 && dp[n - 1][m - 1][MAXN - need] == 1) cout << "YES\n";
  else cout << "NO\n";
}
```
