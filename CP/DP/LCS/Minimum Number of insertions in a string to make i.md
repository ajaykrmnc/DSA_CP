# Minimum Number  of  insertions  in  a  string  to  make  it  a  palindrome (LCS)

**Problem Statement:**
Given a string, find the minimum number of insertions required to make it a palindrome. This problem can be solved using
the concept of Longest Common Subsequence (LCS). Find the LCS between the string and its reverse - this gives the
longest palindromic subsequence. The minimum insertions needed equals (string length - LCS length). Alternatively, use
dynamic programming where dp[i][j] represents minimum insertions needed to make substring from i to j a palindrome. The
solution demonstrates how LCS can be applied to palindrome-related problems.

```cpp
//User function template for C++

class Solution{
public:
  int lcs(string s,string str,int n,int m,vector<vector<int>>&dp){
    if(n==0||m==0)return 0;
    if(dp[n][m]!=-1)return dp[n][m];
    int ans=0;
    if(s[n-1]==str[m-1])ans=lcs(s,str,n-1,m-1,dp)+1;
    else ans=max(lcs(s,str,n-1,m,dp),lcs(s,str,n,m-1,dp));
    return dp[n][m]=ans;
  }
  int findMinInsertions(string S){
    string s=S;
    int n=s.size();
    vector<vector<int>>dp(n+1,vector<int>(n+1,-1));
    reverse(s.begin(),s.end());
    int ans=lcs(s,S,n,n,dp);
    return n-ans;
  }
};
```

