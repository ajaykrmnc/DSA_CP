# Count All Palindromic Subsequence in a given string (LCS)

**Problem Statement:**
Given a string, count the number of palindromic subsequences in it. A subsequence is palindromic if it reads the same forwards and backwards. This problem can be solved using dynamic programming where dp[i][j] represents the count of palindromic subsequences in the substring from index i to j. If characters at i and j are the same, we add 1 (for the new palindrome formed by these characters) plus twice the count from dp[i+1][j-1] (as each inner palindrome can be extended). If characters differ, we use inclusion-exclusion principle: dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]. Handle modular arithmetic to prevent overflow.

link: https://www.geeksforgeeks.org/problems/count-palindromic-subsequences/1

```cpp
class Solution{
    public:
    /*You are required to complete below method */
    long long int mod=1000000007;
    long long int solver(string& s,int i,int j,vector<vector<long long int>>&dp){
        long long int ans=0;
        if(i>j)return 0;
        if(i==j)return 1;
        if(dp[i][j]!=-1)return dp[i][j];
        if(s[j]==s[i]){
            ans=(solver(s,i+1,j,dp)+solver(s,i,j-1,dp)+1)%mod;
        }
        else ans=(solver(s,i+1,j,dp)+solver(s,i,j-1,dp)-solver(s,i+1,j-1,dp)%mod+mod)%mod;
        return dp[i][j]=ans;
    }
    long long int  countPS(string str)
    {
        string s=str;
        int n=s.size();
        vector<vector<long long int>>dp(n+1,vector<long long int>(n+1,-1));
        long long int ans=solver(s,0,n-1,dp);
        return ans;
    }
     
};
```