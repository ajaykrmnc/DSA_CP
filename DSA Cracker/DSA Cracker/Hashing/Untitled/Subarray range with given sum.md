# Subarray range with given sum
**Problem Statement:**
Given an array of integers and a target sum, find the number of subarrays that sum up to the given target. This problem uses
the prefix sum technique with hashing for efficient solution. Maintain a running sum and use a hash map to store frequency
of prefix sums seen so far. For each element, check if (current_sum - target) exists in the map - if yes, add its frequency
to the result. This approach handles both positive and negative numbers. Time complexity is O(n) and space complexity is O(n)
for the hash map. This technique is fundamental for subarray sum problems.

```cpp
class Solution{
    public:
    //Function to count the number of subarrays which adds to the given sum.
    int subArraySum(int arr[], int n, int sum)
    {
        //may2021

        int result=0, tempsum=0;

        unordered_map<int, int>temp;

        for(int i=0 ; i<n ; i++)
         {
             tempsum+=arr[i];
             if(tempsum==sum) result++;

             if(temp.count(tempsum-sum)) result+=temp[tempsum-sum];
             temp[tempsum]++;

         }

        return result;
    }
};
```