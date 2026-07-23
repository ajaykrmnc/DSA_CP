# H - Grid I

**Problem Statement:**
Given an H×W grid where some cells are blocked (marked with '#') and others are free (marked with '.'), find the number of
paths from the top-left corner (1,1) to the bottom-right corner (H,W). You can only move right or down, and cannot pass
through blocked cells. This is a classic grid DP problem where dp[i][j] represents the number of ways to reach cell (i,j).
The recurrence is: dp[i][j] = dp[i-1][j] + dp[i][j-1] if the cell is free, and 0 if blocked. Answer should be modulo 10^9+7.

Tags: grid

```cpp
const int mod=1e9+7;
int32_t main()
{
    speed()
    int t;
    t=1;
    while(t--){
        int n;
        cin>>n;
        int m;
        cin>>m;
        int dp[n][m];
        memset(dp,0,sizeof dp);
        vector<string>v(n);
        for(int i=0;i<n;i++){
            cin>>v[i];
        }
        if(v[0][0]=='#'){
            dp[0][0]=0;
        }else {
            dp[0][0]=1;
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(v[i][j]=='#'){
                    continue;
                }
                if(i>0)
                if(v[i-1][j]=='.'){
                    dp[i][j]+=dp[i-1][j];
                }
                if(j>0)
                if(v[i][j-1]=='.'){
                    dp[i][j]+=dp[i][j-1];
                }
                dp[i][j]%=mod;
            }
        }
        cout<<dp[n-1][m-1]<<nline;
    }

    return 0;
}
```

