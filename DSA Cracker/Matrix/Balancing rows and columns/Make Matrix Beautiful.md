# Make Matrix Beautiful

**Problem Statement:**
Given an n×n matrix, find the minimum number of operations required to make the matrix beautiful. A matrix is beautiful if the sum of each row equals the sum of each column. In each operation, you can increment any element by 1. The strategy is to find the maximum row sum and maximum column sum, then determine the target sum that all rows and columns should have. Calculate the total operations needed by finding the difference between the target sum and current sums.

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