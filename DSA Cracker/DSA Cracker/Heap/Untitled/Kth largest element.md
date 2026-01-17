# Kth largest element

**Problem Statement:**
Given an array of integers and a number k, find the kth largest element in the array. This is a classic heap problem that can
be solved efficiently using a min-heap of size k. Maintain a min-heap with the k largest elements seen so far. For each element,
if the heap size is less than k, add the element. If the heap is full and the current element is larger than the heap's minimum,
remove the minimum and add the current element. The root of the min-heap will be the kth largest element. Time complexity is
O(n log k) and space complexity is O(k), which is better than sorting the entire array.

```cpp
class Solution
{
    public:
    //Function to return kth largest element from an array.
    int KthLargest(int arr[], int n, int k) {
        priority_queue<int,vector<int>,greater<int>>minh(arr,arr+k);
        for(int i=k;i<n;i++){
            if(arr[i]>minh.top()){
                minh.pop();
                minh.push(arr[i]);
            }
        }
        return minh.top();
    }
};
```