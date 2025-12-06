# Kth largest element

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