# Length  of  largest  subsequence  of  A which is a substring  in  B (LCS)

```cpp
int solve(string &s,string &str,int m,int n, vector<vector<int>>&dp){
    if(m==0||n==0)return 0;
    if(dp[m][n]!=-1)return dp[m][n];
    int count=0,count2=0,ans;
    if(s[m-1]==str[n-1])count=1+solve(s,str,m-1,n-1,dp);
    count2=solve(s,str,m-1,n,dp);
    ans=max(count,count2);
    return dp[m][n]=ans;
}
int maxSubsequenceSubstring(string X, string Y, int N, int M){
    int maxi=INT_MIN;
    vector<vector<int>>dp(N+1,vector<int>(M+1,-1));
    for(int i=M;i>0;i--){
        maxi=max(maxi,solve(X,Y,N,i,dp));
    }
    return maxi;
```