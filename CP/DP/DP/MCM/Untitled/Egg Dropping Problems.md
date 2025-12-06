# Egg  Dropping  Problems

```cpp
class Solution
{
    public:
    //Function to find minimum number of attempts needed in 
    //order to find the critical floor.
    int solve(vector<vector<int>>&dp,int n,int k){
        if(k==0||k==1)return k;
        if(dp[n][k]!=-1) return dp[n][k];
        if(n==1)return k;
        int ans=INT_MAX;
        for(int f=1;f<=k;f++){
            int temp_ans=1+max(solve(dp,n-1,f-1),solve(dp,n,k-f));
            ans=min(temp_ans,ans);
        }
        return dp[n][k]=ans;
    }
    int eggDrop(int n, int k) 
    {
        // your code here
        vector<vector<int>>dp(n+1,vector<int>(k+1,-1));
        int ans=solve(dp,n,k);
        return ans;
        
    }
};
```