# K largest elements

**Problem Statement:**
Given an array of integers and a number k, find the k largest elements from the array. The elements can be returned in any order. This problem can be efficiently solved using a min-heap of size k. Iterate through the array: if heap size is less than k, add the element; otherwise, if the current element is larger than the heap's minimum (top), remove the minimum and add the current element. This maintains the k largest elements in the heap. Time complexity is O(n log k) and space complexity is O(k), which is better than sorting the entire array.

```cpp
class Solution
{
    public:
    //Function to return k largest elements from an array.
   vector<int> kLargest(int arr[], int n, int k)
    {
        vector<int>v;
        priority_queue<int,vector<int>,greater<int>>q;
        for(int i=0;i<n;i++){
            if(q.size()<k){
                q.push(arr[i]);
            }
            else{
                if(arr[i]>q.top()){
                    q.pop();
                    q.push(arr[i]);
                }
            }
        }
        while(!q.empty()){
            v.push_back(q.top());
            q.pop();
        }
        reverse(v.begin(),v.end());
        return v;
    }
};
```