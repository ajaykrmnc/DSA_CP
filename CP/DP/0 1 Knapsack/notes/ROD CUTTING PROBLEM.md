# ROD  CUTTING  PROBLEM
**Problem Statement:**
Given a rod of length n and an array of prices for pieces of different lengths, determine the maximum revenue obtainable by
cutting the rod and selling the pieces. You can cut the rod into any combination of pieces, and each piece length can be used
multiple times. This is an unbounded knapsack problem where the rod length is the capacity and piece lengths are items with
unlimited supply. The DP recurrence is: dp[i] = max(dp[i], dp[i-length[j]] + price[j]) for all valid cuts. Time complexity
is O(n²) and space complexity is O(n). This problem teaches optimal cutting strategies and resource optimization.

```cpp
// User function Template for C++

class Solution{
  public:
    int ans(int i,int n,int price[],vector<vector<int>>&dp,int sum){
        if(i<0)return 0;
        if(dp[i][sum]!=-1)return dp[i][sum];
        if(sum+i+1>n)return dp[i][sum]=ans(i-1,n,price,dp,sum);
        int res=max(price[i]+ans(i,n,price,dp,sum+i+1),ans(i-1,n,price,dp,sum));
        return dp[i][sum]=res;

    }
    int cutRod(int price[], int n) {
        vector<vector<int>>dp(n+1,vector<int>(10005,-1));
        int res=ans(n-1,n,price,dp,0);
        return res;
    }
};
```