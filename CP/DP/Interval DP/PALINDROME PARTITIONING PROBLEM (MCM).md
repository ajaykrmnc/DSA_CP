# PALINDROME  PARTITIONING  PROBLEM  (MCM)

<aside>
💡 Given a string **str**, a partitioning of the string is a palindrome partitioning if every sub-string of the 
partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of the given string.

</aside>

```cpp
// User function Template for C++

class Solution{
public:
  int solve(string &s,int i,int j,vector<vector<int>>&dp){
    if(dp[i][j]!=-1)return dp[i][j];
    string str=s.substr(i,j-i+1);
    string str2=str;
    reverse(str.begin(),str.end());
    if(str==str2)
      return 0;
    int ans=INT_MAX;
    for(int k=i;k<j;k++){
      int temp_ans=solve(s,i,k,dp)+solve(s,k+1,j,dp)+1;
      ans=min(ans,temp_ans);
    }
    return dp[i][j]=ans;
  }
  int palindromicPartition(string str)
  {
    int n=str.size();
    vector<vector<int>>dp(n+1,vector<int>(n+1,-1));
    return solve(str,0,n-1,dp);

  }
};
```

