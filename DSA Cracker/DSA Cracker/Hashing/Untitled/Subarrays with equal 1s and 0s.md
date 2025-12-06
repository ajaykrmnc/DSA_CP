# Subarrays with equal 1s and 0s

```cpp
class Solution{
  public:
    //Function to count subarrays with 1s and 0s.
    long long int countSubarrWithEqualZeroAndOne(int arr[], int n){
        long long int res = 0, sum = 0;
        unordered_map<int, int> ump;
        ump[0] = 1;
        for(int i = 0 ; i < n ; i++){
            if(arr[i] == 0)sum--;
            else sum++;
            if(ump[sum] != 0)res += ump[sum];
            ump[sum]++;
        }
        
        return res;
    }
 
};
```