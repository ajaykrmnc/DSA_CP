# Minimum Cost to cut the stick (MCM)

```cpp
class Solution {
public:
    int solve(int i,int j,vector<int>&arr,vector<vector<int>>&dp,int target){
        if(i>=j)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        int ans=INT_MAX;
        int sum=0;
        for(int k=i;k<j;k++){
            sum+=arr[k];
            int temp_ans=target+solve(i,k,arr,dp,sum)+solve(k+1,j,arr,dp,target-sum);
            ans=min(ans,temp_ans);
        }
        return dp[i][j]=ans;
    }
    int minCost(int n, vector<int>& cuts) {
        vector<int>arr;
        sort(cuts.begin(),cuts.end());
        for(int i=0;i<cuts.size();i++){
            if(i==0)arr.push_back(cuts[0]);
            else arr.push_back(cuts[i]-cuts[i-1]);
        }
        if(n!=cuts.back())
        arr.push_back(n-cuts.back());
        int sz=arr.size();
        vector<vector<int>>dp(sz+2,vector<int>(sz+2,-1));
        return solve(0,sz-1,arr,dp,n);
    }
};
```