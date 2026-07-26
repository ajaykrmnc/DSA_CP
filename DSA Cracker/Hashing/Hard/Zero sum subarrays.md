# Zero sum subarrays

**Problem Statement:**
Given an array of integers, count the number of subarrays that have a sum equal to zero. Use the prefix sum technique
where if two prefix sums are equal, the subarray between them has sum zero. Maintain a frequency map of prefix sums
and for each prefix sum, add the count of how many times it has appeared before. This gives the number of zero-sum
subarrays ending at the current position. Time complexity is O(n) and space complexity is O(n).

```cpp
class Solution{
public:
    //Function to count subarrays with sum equal to 0.
    long long int findSubarray(vector<long long int> &arr, int n ) {
        long long int result = 0;
        map<long long int, int> freq;
        long long int sum = 0;
        freq[0]++;
        for(int i = 1; i <= n; i++){
            sum += arr[i-1];
            freq[sum]++;
            result += freq[sum] - 1;
        }
        return result;
    }
};
```