# Printing Shortest Common Supersequence (LCS)

Given two strings **X** and **Y** of lengths **m** and **n** respectively, find the length of the **smallest string** which has both, **X and Y** as its **sub-sequences**.**Note:** **X** and **Y** can have both uppercase and lowercase letters.

```cpp
//User function template for C++

class Solution
{
    public:
    int lcs(int n,int m,string str,string s,vector<vector<int>>&dp){
        if(n<=0||m<=0)return 0;
        if(dp[n][m]!=-1)return dp[n][m];
        int ans=0;
        if(str[n-1]==s[m-1])ans=lcs(n-1,m-1,str,s,dp)+1;
        else ans=max(lcs(n,m-1,str,s,dp),lcs(n-1,m,str,s,dp));
        return dp[n][m]=ans;
    }
    
    //Function to find length of shortest common supersequence of two strings.
    int shortestCommonSupersequence(string X, string Y, int m, int n)
    {
        //code here
        vector<vector<int>>dp(m+1,vector<int>(n+1,-1));
        int ans=lcs(m,n,X,Y,dp);
        return (X.size()+Y.size()-ans);
    }
};
```