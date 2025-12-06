# Next Greater Element

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