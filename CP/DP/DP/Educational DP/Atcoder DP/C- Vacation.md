# C- Vacation

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