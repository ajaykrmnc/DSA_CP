# ROD  CUTTING  PROBLEM

```cpp
// User function Template for C++

class Solution{
  public:
    int ans(int i,int n,int price[],vector<vector<int>>&dp,int sum){
        if(i<0)return 0;
        if(dp[i][sum]!=-1)return dp[i][sum];
        if(sum+i+1>n)return dp[i][sum]=ans(i-1,n,price,dp,sum);
        int res=max(price[i]+ans(i,n,price,dp,sum+i+1),ans(i-1,n,price,dp,sum));
        return dp[i][sum]=res;
        
    }
    int cutRod(int price[], int n) {
        vector<vector<int>>dp(n+1,vector<int>(10005,-1));
        int res=ans(n-1,n,price,dp,0);
        return res;
    }
};
```