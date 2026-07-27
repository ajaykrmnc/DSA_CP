# Minimum Number of Insertions and Deletions in a string A   to convert it to string  B (LCS)

**Problem Statement:**
Given two strings A and B, find the minimum number of insertions and deletions required to convert string A to string B.
This problem uses the concept of Longest Common Subsequence (LCS). First, find the LCS of both strings. The number of
deletions needed is (length of A - LCS length) and the number of insertions needed is (length of B - LCS length). The
total operations required is the sum of insertions and deletions. This approach ensures minimum operations by preserving
the maximum common characters between the strings.

```cpp
class Solution{

public:
	int solve(int m,int n,string s1,string s2,vector<vector<int> > &dp){
    if(m == 0 or n== 0){
      return 0;
    }

    if(dp[m][n]!=-1){
      return dp[m][n];
    }
    if(s1[m-1] == s2[n-1]){
      dp[m][n] = 1+ solve(m-1,n-1,s1,s2,dp);
    }
    else{
      dp[m][n] = max(solve(m,n-1,s1,s2,dp),solve(m-1,n,s1,s2,dp));
    }
    return dp[m][n];
	}
	int minOperations(string str1, string str2)
	{
    // Your code goes here
    int m = str1.length();
    int n = str2.length();
    vector<vector<int> > dp(m+1,vector<int>(n+1,-1));
   	int ans = solve(m,n,str1,str2,dp);
    return (m-ans)+(n-ans);

	}
};
```
