# Subarray range with given sum

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