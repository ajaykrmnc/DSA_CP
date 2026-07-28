# Nearly sorted

**Problem Statement:**
Given an array where each element is at most k positions away from its target position in a sorted array, sort the array efficiently. Since elements are nearly sorted (displaced by at most k positions), we can use a min heap of size k+1. The idea is to maintain a heap with first k+1 elements, extract the minimum (which is the next element in sorted order), and add the next element from the array. This approach gives O(n log k) time complexity, which is better than O(n log n) when k is small compared to n.

```cpp
class Solution
{
    public:
    //Function to return the sorted array.
    vector <int> nearlySorted(int arr[], int num, int k){
        // Your code here
        vector<int>ans;
        priority_queue<int,vector<int>,greater<int>>pq(arr,arr+k+1);
        for(int i=0;i<num;i++){
            ans.push_back(pq.top());
            pq.pop();
            if(i+k+1<num){
                pq.push(arr[i+k+1]);
            }
        }
        return ans;
    }
};
```