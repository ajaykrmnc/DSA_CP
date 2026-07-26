# Merge k Sorted Arrays

**Problem Statement:**
Given k sorted arrays, merge them into a single sorted array. This is a classic problem that can be solved efficiently
using a min-heap (priority queue). The approach involves inserting the first element of each array into the heap along
with array and element indices. Repeatedly extract the minimum element from heap and insert the next element from the
same array. This ensures we always get the globally minimum element among all arrays. Time complexity is O(n log k)
where n is total elements and k is number of arrays. This problem demonstrates the power of heaps in merging multiple
sorted sequences efficiently.

```cpp
//User function Template for C++

class Solution
{
public:
  //Function to merge k sorted arrays.
  vector<int> mergeKArrays(vector<vector<int>> arr, int k) {
    //code here
    priority_queue<int> pq;
    for(int i=0;i<k;i++)
    {
      for(int  j =0;j<k;j++)
      {
        arr[i][j] *=-1;
        pq.push(arr[i][j]);
      }
    }
    vector<int> ans;
    while(!pq.empty())
    {
      int temp =-1* pq.top();
      pq.pop();
      ans.push_back(temp);
    }
    return ans;
  }
};
```

