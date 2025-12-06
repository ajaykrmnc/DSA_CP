# Combination Sum

Given an array of integers and a sum B, find all unique combinations in the array where the sum is equal to B. The same number may be chosen from the array any number of times to make B.

**Note:**        

**1.** All numbers will be positive integers.        ****

**2.** Elements in a combination (a1, a2, …, ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).        

**3.** The combinations themselves must be sorted in ascending order.

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