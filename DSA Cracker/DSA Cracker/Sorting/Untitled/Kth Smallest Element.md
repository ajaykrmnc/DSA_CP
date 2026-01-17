# Kth Smallest Element

**Problem Statement:**
Given an array of integers and a number k, find the kth smallest element in the array. This can be solved using multiple approaches: sorting (O(n log n)), min-heap of size n (O(n log n)), max-heap of size k (O(n log k)), or quickselect algorithm (O(n) average case). The max-heap approach is efficient for small k values - maintain a max-heap of size k, and for each element, if it's smaller than the heap's top, replace the top. The final top element is the kth smallest.

```cpp
class Solution
{
    public:
    //Function to find the kth smallest element in the array.
    int kthSmallest(int arr[], int n, int k)
    {
        priority_queue<int> pq(arr, arr+k);
        
        for(int i=k; i<n; i++){
            if(arr[i] < pq.top()){
                pq.pop();
                pq.push(arr[i]);
            }
        }
        
        return pq.top();
    }
};
```