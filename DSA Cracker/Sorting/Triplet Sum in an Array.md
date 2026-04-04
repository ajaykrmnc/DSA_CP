# Triplet Sum in an Array

**Problem Statement:**
Given an array of integers and a target sum X, find if there exists a triplet (three elements) in the array that sums up to X.
This is a classic 3Sum problem that can be solved efficiently using sorting and two pointers technique. First sort the array,
then for each element, use two pointers to find if there's a pair in the remaining array that sums to (X - current_element).
The time complexity is O(n²) after sorting, which is optimal for this problem. This approach avoids the O(n³) brute force solution
and demonstrates the power of combining sorting with two pointers technique.

```cpp
class Solution{
    public:
    //Function to find if there exists a triplet in the 
    //array A[] which sums up to X.
    bool find3Numbers(int arr[], int n, int x)
    {
        sort(arr,arr+n);
        int i=0;
        while(i<n-2){
            int target=x-arr[i];
            int j=i+1,k=n-1;
            while(j<n&&j<k){
                if(arr[j]+arr[k]>target){
                    k--;
                }else if(arr[j]+arr[k]<target){
                    j++;
                }else 
                return 1;
            }
            i++;
        }
        return 0;
    }

};
```