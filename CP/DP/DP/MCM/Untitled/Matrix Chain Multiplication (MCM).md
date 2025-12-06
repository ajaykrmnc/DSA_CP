# Matrix  Chain  Multiplication (MCM)

```cpp
// User function Template for C++

class Solution{
public:
    int matrixMultiplication(int n,int arr[]){
    int dp[n+1][n+1];
    for(int i=1;i<n;i++){
        for(int j=1;j<n;j++){
            if(i==j){
                dp[i][j]=0;
            }else
            dp[i][j]=INT_MAX;
        }
    }
    for(int l=1;l<n;l++){
        for(int i=1;i<n-l;i++){
            int j=i+l;
            for(int k=i;k<j;k++){
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j]);
            }
        }
    }
    return dp[1][n-1];
}
};
```

```cpp
// User function Template for C++

class Solution{
public:
    int ans(int i,int j,int arr[],vector<vector<int>>&dp){
        if(i==j)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        int res=INT_MAX;
        for(int k=i;k<j;k++){
            int temp_ans=ans(i,k,arr,dp)+ans(k+1,j,arr,dp)+arr[i-1]*arr[k]*arr[j];
            res=min(res,temp_ans);
        }
        return dp[i][j]=res;
    }
    int matrixMultiplication(int N, int arr[])
    {
        vector<vector<int>>dp(N,vector<int>(N,-1));
        return ans(1,N-1,arr,dp);
    }
};
```