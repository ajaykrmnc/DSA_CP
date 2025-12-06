# Make Matrix Beautiful

```cpp
class Solution
{
    public:
    //Function to find minimum number of operations that are required 
    //to make the matrix beautiful.
    int findMinOpeartion(vector<vector<int> > matrix, int n)
    {
        // code here 
        int mini=0;
        for(int i=0;i<n;i++){
            int sum=0;
            for(int j=0;j<n;j++){
                sum+=matrix[i][j];
            }
            mini=max(sum,mini);
        }
        for(int j=0;j<n;j++){
            int sum=0;
            for(int i=0;i<n;i++){
                sum+=matrix[i][j];
            }
            mini=max(sum,mini);
        }
        int req=n*mini;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                req-=matrix[i][j];
            }   
        }
        return req;
    } 
};
```