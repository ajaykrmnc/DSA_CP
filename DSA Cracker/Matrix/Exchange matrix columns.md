# Exchange matrix columns

**Problem Statement:**
Given an n×m matrix, exchange the first column with the last column. This is a simple matrix manipulation problem where you need to swap elements at positions (i, 0) with elements at positions (i, m-1) for all rows i. The solution involves iterating through each row and swapping the first and last elements using a simple swap operation. Time complexity is O(n) where n is the number of rows, and space complexity is O(1) as we only use constant extra space.

```cpp
class Solution
{
    public:
    //Function to exchange first column of a matrix with its last column.
    void exchangeColumns(vector<vector<int> > &matrix)
    {
        // code here
        int n=matrix.size(),m=matrix[0].size();
        for(int i=0;i<n;i++){
            swap(matrix[i][0],matrix[i][m-1]);
        }
    }
};
```