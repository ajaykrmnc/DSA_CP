# Nearly sorted

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