# Unique Subsets
**Problem Statement:**
Given an array of integers that may contain duplicates, find all possible unique subsets. Each subset should be sorted
and the result should not contain duplicate subsets. Use backtracking to generate all subsets: for each element, decide
whether to include it or not. To handle duplicates, sort the array first and skip duplicate elements at the same recursion
level. This ensures that duplicate subsets are not generated. The algorithm explores all 2^n possibilities while maintaining
uniqueness through careful duplicate handling.

Given an array **arr[]** of integers of size **N** that might contain **duplicates**, the task is to find all possible unique subsets.

**Note:** Each subset should be sorted.

```cpp
class Solution
{
    public:
    //Function to find all possible unique subsets.
    void solve(vector<int>&arr,int index,int n,vector<int>&v,vector<vector<int>>&ans){
        if(index == n){
            ans.push_back(v);
            return ;
        }
        v.push_back(arr[index]);
        solve(arr,index+1,n,v,ans);
        v.pop_back();
        solve(arr,index+1,n,v,ans);
    }
    vector<vector<int> > AllSubsets(vector<int> arr, int n)
    {
        // code here
        vector<vector<int>>ans;
        vector<int>v;
        solve(arr,0,n,v,ans);
        for(long long i=0;i<ans.size();i++){
            sort(ans[i].begin(),ans[i].end());
        }
        sort(ans.begin(),ans.end());
        ans.erase(unique(ans.begin(),ans.end()),ans.end());
        return ans;

    }
};
```