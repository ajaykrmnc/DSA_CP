# MINIMUM  SUBSET  SUM  DIFFERENCE-(0/1 KNAPSACK)

```cpp
class Solution{

  public:
    int isPossible(int arr[],vector<vector<int>>&dp,int i,int diff){
        if(i<0)return 0;
        if(i==0)return (abs(diff-arr[0]));
        if(dp[i][diff]!=-1)return dp[i][diff];
        int ans=min(isPossible(arr,dp,i-1,abs(diff-arr[i])),isPossible(arr,dp,i-1,abs(diff+arr[i])));
        return dp[i][diff]=ans;
        
    }
	int minDifference(int arr[], int n)  { 
	    int sum=0;
	    for(int i=0;i<n;i++){
	        sum+=arr[i];
	    }
	    vector<vector<int>>dp(n+1,vector<int>(sum+1,-1));
	    int ans=isPossible(arr,dp,n-1,0);
	    return ans;
	    
	} 
};
```