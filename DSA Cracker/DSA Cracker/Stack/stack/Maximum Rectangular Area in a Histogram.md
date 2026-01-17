# Maximum Rectangular Area in a Histogram

**Problem Statement:**
Given an array representing heights of bars in a histogram, find the area of the largest rectangle that can be formed.
For each bar, the maximum rectangle with that bar as the smallest height extends from the nearest smaller element on the left
to the nearest smaller element on the right. This problem is efficiently solved using a stack to find the nearest smaller
elements. The stack maintains indices of bars in increasing order of heights. When a smaller bar is encountered, calculate
areas for all bars that can use previous bars as the smallest height. Time complexity is O(n) and space complexity is O(n).

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& nums) {
        int n=nums.size();
        vector<int>lb(n),rb(n);
        stack<int>st;
        for(int i=0;i<n;i++){
            while(!st.empty() and nums[i]<=nums[st.top()]){
                st.pop();
            }
            if(st.empty())lb[i]=-1;
            else{
                lb[i]=st.top();
            }
            st.push(i);
        }
        while(st.size()){st.pop();}
        for(int i=n-1;i>=0;i--){
            while(!st.empty() and nums[i]<=nums[st.top()]){
                st.pop();
            }
            if(st.empty())rb[i]=n;
            else{
                rb[i]=st.top();
            }
            st.push(i);
        }
        int ans=0;

        for(int i=0;i<n;i++){
            ans=max(ans, nums[i]*(rb[i]-lb[i]-1));
        }
        return ans;    
    }
};
```