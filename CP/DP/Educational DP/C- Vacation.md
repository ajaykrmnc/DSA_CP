# C- Vacation

**Problem Statement:**
Taro's summer vacation lasts for N days. For each day i (1 ≤ i ≤ N), he can choose to do one of three activities: A, B, or C.
Each activity gives him happiness points: a[i], b[i], or c[i] respectively on day i. However, he cannot do the same activity
on two consecutive days. Find the maximum total happiness Taro can achieve during his vacation. This is a dynamic programming
problem where dp[i][j] represents the maximum happiness achievable up to day i when the last activity chosen was j (0=A, 1=B, 2=C).
The recurrence considers all valid transitions from the previous day's activities.

```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e5 + 1;
const int inf = 1e16;
const int MOD = 1e9 + 7 ;
int maxx = 0  , cnt =  0;

signed main()
{
   int n ;
   cin >> n ;
   int a[n] , c[n] , b[n];
   for(int i = 0  ; i < n ; i++){
         cin >> a[i] >> b[i] >> c[i];
   }

   int dp[n+1][4];
   memset(dp , 0 , sizeof dp);
   dp[1][1] = a[0];
   dp[1][2] = b[0];
   dp[1][3] = c[0];
   for(int i =  2 ; i <= n ; i++){
        dp[i][1] = a[i-1] + max(dp[i-1][2] , dp[i-1][3]);
        dp[i][2] = b[i-1] + max(dp[i-1][1] , dp[i-1][3]);
        dp[i][3] = c[i-1] + max(dp[i-1][1] , dp[i-1][2]);
   }
   int ans = max({dp[n][1] , dp[n][2] , dp[n][3]});
   cout << ans << endl;
}
```