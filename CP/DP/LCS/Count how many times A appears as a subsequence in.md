# Count  how  many  times  A  appears  as  a  subsequence  in  B (LCS)

```cpp
class Solution{
public:
    int ans=0;
    int lcs(string s,string str,int n, int m,vector<vector<int>>&dp){
        if((m==0)){return 1;}
        if(n==0){return 0;}
        if(dp[n][m]!=-1) return dp[n][m];
        if(s[n-1]==str[m-1])return dp[n][m]=lcs(s,str,n-1,m-1,dp)+lcs(s,str, n-1,m, dp);
        else return dp[n][m]=lcs(s,str, n-1,m, dp);;
    }
    int countWays(string s, string str){
        vector<vector<int>>dp(s.size()+1,vector<int>(str.size()+1,-1));
        int res=lcs(s,str,s.size(),str.size(),dp);
        return res;
    }
};
```