# Maximum Subarray

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& v) {
        int sum = 0;
        int ans = INT_MIN;
        int n = v.size();
        for(int i = 0; i < n; ++i){
            if(sum < 0){
                sum = v[i];
            }else{
                sum += v[i];
            }
            ans = max(sum, ans);
        }
        return ans;
    }
};
```