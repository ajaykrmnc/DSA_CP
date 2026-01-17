# Boundary traversal of matrix

**Problem Statement:**
Given an n×m matrix, traverse and return the boundary elements in clockwise order. The boundary consists of the first row, last column, last row (in reverse), and first column (in reverse, excluding corners already covered). For a single row or column matrix, simply return all elements. The traversal should start from the top-left corner and move clockwise around the perimeter. Handle edge cases where the matrix has only one row or one column to avoid duplicate elements. Time complexity is O(n+m) and space complexity is O(1) excluding the result array.

```cpp
class Solution
{   
    public:
    //Function to return list of integers that form the boundary 
    //traversal of the matrix in a clockwise manner.
    vector<int> boundaryTraversal(vector<vector<int> > matrix, int n, int m) 
    {
        // code here
        vector<int>ans;
        for(int i=0;i<m;i++){
            ans.push_back(matrix[0][i]);
        }
        for(int j=1;j<n;j++){
            ans.push_back(matrix[j][m-1]);
        }
        for(int i=1;i<m and n>1;i++){
            ans.push_back(matrix[n-1][m-i-1]);
        }
        for(int i=1;i<n-1 and m>1;i++){
            ans.push_back(matrix[n-i-1][0]);
        }
        return ans;
    }
};
```