# Merge k Sorted Arrays

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