# Longest Bitonic Subsequence

**Problem Statement:**
Given an array of positive integers, find the maximum length of a bitonic subsequence. A bitonic subsequence is first strictly
increasing, then strictly decreasing. The solution involves computing two arrays: LIS[i] = length of longest increasing subsequence
ending at i, and LDS[i] = length of longest decreasing subsequence starting at i. For each position i, the longest bitonic
subsequence passing through i has length LIS[i] + LDS[i] - 1. The answer is the maximum value across all positions. Time
complexity is O(n²) using standard LIS/LDS computation, or O(n log n) using binary search optimization.

```cpp
Given an array of positive integers. Find the maximum length of Bitonic subsequence.
A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing.
```

```cpp
class Solution{
	public:
	vector<int> LIS(vector<int>nums)
   {
    int n=nums.size();
    vector<int>dp(n,1);
    for(int i=1;i<n;i++)
    {
        for(int j=0;j<i;j++)
        {
            if(nums[j]<nums[i])
                dp[i]=max(dp[i],dp[j]+1);
        }
    }
    return dp;
}
int LongestBitonicSequence(vector<int>nums)
{
       vector<int> lis=LIS(nums);
       reverse(nums.begin(),nums.end());
       vector<int> lds=LIS(nums);
       int ans=INT_MIN;
       int n=nums.size();
       reverse(lds.begin(),lds.end());
       for(int i=0;i<n;i++)
           ans=max(ans,lis[i]+lds[i]-1);
       
       return ans;
}
	    
};
```