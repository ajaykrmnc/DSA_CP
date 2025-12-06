# SUBSET  SUM-(0/1 KNAPSACK)

```cpp
//User function template for C++

class Solution{   
public:
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