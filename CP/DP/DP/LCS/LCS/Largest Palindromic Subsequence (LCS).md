# Largest  Palindromic  Subsequence (LCS)

```cpp
//User function Template for C++
class Solution{
  public:
    int lcs(int n,int m,string s,string str,vector<vector<int>>&dp){
        if(n<=0||m<=0)return 0;
        if(dp[n][m]!=-1)return dp[n][m];
        int ans=0;
        if(s[n-1]==str[m-1])
        ans=lcs(n-1,m-1,s,str,dp)+1;
        else
        ans=max(lcs(n,m-1,s,str,dp),lcs(n-1,m,s,str,dp));
        return dp[n][m]=ans;
    }
    int longestPalinSubseq(string A) {
        string s=A;
        reverse(s.begin(),s.end());
        int n=s.size();
        vector<vector<int>>dp(n+1,vector<int>(n+1,-1));
        int ans=lcs(n,n,s,A,dp);
        return ans;
        
    }
};
```