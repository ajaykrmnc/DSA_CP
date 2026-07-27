# SUBSET  SUM-(0/1 KNAPSACK)

**Problem Statement:**
Given an array of integers and a target sum, determine if there exists a subset of the array that sums exactly
to the target.
This is a classic 0/1 knapsack variation where each element can be either included or excluded from the
subset. The problem can
be solved using dynamic programming where `dp[i][sum]` represents whether it's possible to achieve the sum using
first i elements.
The recurrence relation is: `dp[i][sum] = dp[i-1][sum] || dp[i-1]sum-arr[i]]`. Time complexity is O(n\*sum) and
space can be
optimized to O(sum) using 1D array. This problem forms the basis for many other DP problems.

```cpp
//User function template for C++

class Solution{   public:
  bool isPossible(vector<int>&arr,vector<vector<int>>&dp,int i,int sum){
    if(sum==0)return 1;
    if(i<0)return 0;
    if(dp[i][sum]!=-1)return dp[i][sum];
    if(arr[i]>sum){
      return dp[i][sum]=isPossible(arr,dp,i-1,sum);
    }
    return dp[i][sum]=(isPossible(arr,dp,i-1,sum)||isPossible(arr,dp,i-1,sum-arr[i]));

  }

  bool isSubsetSum(vector<int>&arr,int targetSum){
    int n=arr.size();
    vector<vector<int>>dp(n+1,vector<int>(102*(n),-1));
    bool ans=isPossible(arr,dp,n-1,targetSum);
    return ans;
  }
};
```
