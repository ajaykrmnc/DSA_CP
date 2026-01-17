# Next Greater Element

**Problem Statement:**
Given an array, find the next greater element for each element in the array. The next greater element for an element x is the first greater element on the right side of x in the array. If no such element exists, return -1 for that element. This classic problem is efficiently solved using a stack data structure. Traverse the array from right to left, maintaining a stack of elements. For each element, pop smaller elements from the stack, then the top of stack (if exists) is the next greater element. Push the current element to stack and continue. Time complexity is O(n) and space complexity is O(n).

```cpp
class Solution
{
    public:
    //Function to find the next greater element for each element of the array.
    vector<long long> nextLargerElement(vector<long long> arr, int n){
        // Your code here
        stack<long long>st;
        vector<long long>ans(n);
        for(int i = n-1; i>=0 ; i--){
            while(st.size() and arr[st.top()] <= arr[i]){
                st.pop();
            }
            if(st.size()){
                ans[i] = arr[st.top()];
            }else{
                ans[i] = -1;
            }
            st.push(i);
        }
        return ans;
    }
};
```