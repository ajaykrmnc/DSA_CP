# interchanging the rows of a Matrix

**Problem Statement:**
Given an n×m matrix, interchange the first row with the last row, second row with the second-last row, and so on. This operation reverses the order of rows in the matrix. For each pair of rows (i, n-1-i) where i goes from 0 to n/2-1, swap all elements in these rows. The solution involves nested loops: outer loop for row pairs and inner loop for swapping elements within each row pair. Time complexity is O(n×m) and space complexity is O(1) as we perform in-place swapping.

```cpp
class Solution
{   
    public:
    //Function to interchange the rows of a matrix.
    void interchangeRows(vector<vector<int> > &matrix)
    {
        // code here
        int n=matrix.size(),m=matrix[0].size();
        for(int i=0;i<n/2;i++){
            for(int j=0;j<m;j++){
                swap(matrix[i][j],matrix[n-i-1][j]);
            }
        }
        
        
    }
};
```