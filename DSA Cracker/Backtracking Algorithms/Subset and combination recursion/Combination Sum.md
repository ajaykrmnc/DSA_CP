# Combination Sum

**Problem Statement:**
Given an array of positive integers and a target sum B, find all unique combinations where the sum equals B. Elements
can be reused multiple times, and combinations should be in non-descending order. This is a classic backtracking problem
where we explore two choices at each step: include the current element (and stay at the same index to allow reuse) or
skip to the next element. The solution uses recursion with backtracking to generate all valid combinations, ensuring no
duplicates by sorting the array and using proper indexing. Time complexity is exponential due to the nature of
generating all combinations.
Given an array of integers and a sum B, find all unique combinations in the array where the sum is equal to B. The same
number may be chosen from the array any number of times to make B.

**Note:**

```cpp
//User function template for C++

class Solution {
public:
  //Function to return a list of indexes denoting the required
  //combinations whose sum is equal to given number.
  void helper(int i,int n,vector<int>&nums,int tar,vector<int>&temp,vector<vector<int>>&st){
    if(tar==0){
      st.push_back(temp);
      return ;
    }
    if(i==n||tar<0){
      return ;
    }
    temp.push_back(nums[i]);
    helper(i,n,nums,tar-nums[i],temp,st);
    temp.pop_back();
    helper(i+1,n,nums,tar,temp,st);
  }
  vector<vector<int> > combinationSum(vector<int> &A, int B) {
    // Your code here
    sort(A.begin(),A.end());
    A.erase(unique(A.begin(),A.end()),A.end());
    vector<vector<int>>ans;
    vector<int>temp;
    int n=A.size();
    helper(0,n,A,B,temp,ans);
    return ans;
  }
};
```
