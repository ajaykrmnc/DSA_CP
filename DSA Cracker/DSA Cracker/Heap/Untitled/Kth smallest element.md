# Kth smallest element

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