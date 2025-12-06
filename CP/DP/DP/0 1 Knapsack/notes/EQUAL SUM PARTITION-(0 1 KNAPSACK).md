# EQUAL  SUM  PARTITION-(0/1  KNAPSACK)

```cpp
// User function Template for C++

class Solution{
public:
    int isPossible(int arr[],vector<vector<int>>&dp,int i,int sum){
        if(sum==0)return 1;
        if(i<0)return 0;
        if(arr[i]>sum){
            return dp[i][sum]=isPossible(arr,dp,i-1,sum);
        }else 
        return dp[i][sum]=isPossible(arr,dp,i-1,sum-arr[i])||isPossible(arr,dp,i-1,sum);
    }
    int equalPartition(int n, int arr[])
    {
        vector<vector<int>>dp(n+1,vector<int>((n+1)*1000,-1));
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=arr[i];
        }
        if(sum%2)return 0;
        sum/=2;
        bool ans=isPossible(arr,dp,n-1,sum);
        return ans;
    }
};
```