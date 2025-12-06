# Maximum Rectangular Area in a Histogram

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