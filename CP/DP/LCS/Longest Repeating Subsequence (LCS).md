# Longest Repeating Subsequence (LCS)

Given string str, find the length of the longest repeating subsequence such that it can be found twice in the given string.

The two identified subsequences A and B can use the same ith character from string str if and only if that ith character has different indices in A and B. For example, A = "xax" and B = "xax" then the index of first "x" must be different in the original string for A and B.

```cpp
class Solution {
	public:
	    
	    int lcs(string &a,string &b,int idx1,int idx2,int n,vector<vector<int>>&dp){
	        if(idx1==n||idx2==n){
	            return 0;
	        }if(dp[idx1][idx2]!=-1){
	            return dp[idx1][idx2];
	        }
	        int include=0;
	        if(a[idx1]==b[idx2]&&idx1!=idx2){
	            include=1+lcs(a,b,idx1+1,idx2+1,n,dp);
	        }
	        int exclude=max(lcs(a,b,idx1+1,idx2,n,dp),lcs(a,b,idx1,idx2+1,n,dp));
	        return dp[idx1][idx2]=max(include,exclude);
	    }
		int LongestRepeatingSubsequence(string str){
		    int n=str.size();
		    vector<vector<int>>dp(n+1,vector<int>(n+1,-1));
		    return lcs(str,str,0,0,n,dp);
		}

};
```