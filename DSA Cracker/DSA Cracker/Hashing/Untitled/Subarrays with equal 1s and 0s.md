# Subarrays with equal 1s and 0s

**Problem Statement:**
Given a binary array containing only 0s and 1s, count the number of subarrays that have an equal number of 0s and 1s.
Use the concept of prefix sum where 0s are treated as -1 and 1s as +1. If two prefix sums are equal, the subarray between
them has equal 0s and 1s (sum = 0). Use a hashmap to store frequency of prefix sums and count subarrays efficiently.
This problem demonstrates the power of prefix sum technique combined with hashing for subarray problems.

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