# EQUAL  SUM  PARTITION-(0/1  KNAPSACK)

**Problem Statement:**
Given an array of positive integers, determine if it can be partitioned into two subsets with equal sum. This is
equivalent to finding if there exists a subset with sum equal to half of the total array sum. If the total sum is odd,
return false immediately.

Otherwise, use the subset sum DP approach to check if a subset with sum = total_sum/2 exists.
The DP state dp\[i]\[sum]
represents whether it's possible to achieve the sum using first i elements. This problem demonstrates how knapsack
variations can solve partitioning problems.

Time complexity is O(n\*sum) and space can be optimized to O(sum).

```cpp
// User function Template for C++

class Solution{
public:
  int isPossible(int arr[], vector<vector<int>>&dp, int i, int sum){
    if (sum == 0) return 1;
    if (i<0) return 0;
    if (arr[i]> sum) {
      return dp[i][sum] = isPossible(arr ,dp ,i-1 ,sum);
    }else
    return dp[i][sum] = isPossible(arr,dp,i-1,sum-arr[i]) || isPossible(arr,dp,i-1,sum);
  }

  int equalPartition(int n, int arr[]) {
    vector<vector<int>>dp(n+1,vector<int>((n+1)*1000,-1));
    int sum=0;
    for(int i=0;i<n;i++){
      sum += arr[i];
    }
    if(sum % 2) return 0;
    sum/=2;
    bool ans=isPossible(arr,dp,n-1,sum);
    return ans;
  }
};
```

