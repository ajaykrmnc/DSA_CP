# N - Slimes

Tags: mcm

```cpp
#include<bits/stdc++.h>
using namespace std;
 
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include "mylib/mydebug.h"
#else
#define debug(x)
#endif
 
#define int long long
 
// User function Template for C++

class Solution{
public:
    int matrixMultiplication(int n,vector<int>&arr){
    vector<vector<int>>dp(n, vector<int>(n));
    vector<int>pre(n, 0);
    for(int i = 0; i < n; i++){
        if(i == 0)
            pre[i] = arr[i];
        else 
            pre[i] += pre[i - 1] + arr[i];
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(i==j){
                dp[i][j] = 0;
            }else
            dp[i][j]= INT_MAX;
        }
    }
    for(int l=1;l<n;l++){
        for(int i=0;i<n-l;i++){
            int j=i+l;
            for(int k=i;k<j;k++){
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+ ((i == 0) ? pre[j] : pre[j] - pre[i - 1]));
            }
        }
    }
    debug(dp);
    return dp[0][n-1];
}
};
 
int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int t = 1;
    // cin >> t;
    while (t--) {
        Solution obj;
        int n;
        cin >> n;
        vector<int>arr(n);
        for(auto &x: arr){
            cin >> x;
        }
        cout << obj.matrixMultiplication(n, arr);
    }
    return 0;
}
```