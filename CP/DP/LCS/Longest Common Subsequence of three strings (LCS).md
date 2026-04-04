# Longest  Common  Subsequence  of  three  strings (LCS)

**Problem Statement:**
Given three strings, find the length of their longest common subsequence. This is an extension of the classic 2-string LCS problem to three strings. A subsequence is common to all three strings if it appears in the same relative order in each string. Use 3D dynamic programming where dp[i][j][k] represents the LCS length of first i characters of string1, first j characters of string2, and first k characters of string3. If all three characters match, add 1 to dp[i-1][j-1][k-1]; otherwise, take the maximum of three possible transitions. Time complexity is O(n*m*o) where n, m, o are the string lengths.
link: https://www.geeksforgeeks.org/problems/find-number-of-times-a-string-occurs-as-a-subsequence3020/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

```cpp
int lcs(int n,int m,int o,string s,string st,string str,vector<vector<vector<int>>>&dp){
    if(n==0||m==0||o==0)return 0;
    if(dp[n][m][o]!=-1)return dp[n][m][o];
    if((s[n-1]==st[m-1])&&(st[m-1]==str[o-1]))
    return dp[n][m][o]=1+lcs(n-1,m-1,o-1,s,st,str,dp);
    else
    {
        return dp[n][m][o]=max(lcs(n-1,m,o,s,st,str,dp),max(lcs(n,m-1,o,s,st,str,dp),lcs(n,m,o-1,s,st,str,dp)));
    }
}
int LCSof3 (string s, string st, string str, int n, int m, int o)
{
    vector<vector<vector<int>>>dp(n+1,vector<vector<int>>(m+1,vector<int>(o+1,-1)));
    int ans=lcs(n,m,o,s,st,str,dp);
    return ans;

}
```