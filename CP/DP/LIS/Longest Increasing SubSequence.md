# Longest  Increasing  SubSequence
**Problem Statement:**
Given an array of integers, find the length of the longest increasing subsequence (LIS). A subsequence is increasing if
each element is greater than the previous one. The classic DP solution uses dp[i] to represent the length of LIS ending
at index i. For each element, check all previous elements and extend the longest subsequence where current element is greater.
Time complexity is O(n²). An optimized O(n log n) solution uses binary search with a temporary array to maintain the smallest tail.

```cpp
class Solution
{
    public:
    //Function to find length of longest increasing subsequence.
    int longestSubsequence(int n, int a[]){
        int dp[n+1];
        dp[0]=1;
        for(int i=0;i<n;i++){
            dp[i]=1;
            for(int j=0;j<i;j++){
                if(a[i]>a[j]){
                    dp[i]=max(dp[j]+1,dp[i]);
                }
            }
        }
        int ans=0;
        for(int i=0;i<n;i++){
           ans=max(ans,dp[i]);
        }
        return ans;
    }
};
```