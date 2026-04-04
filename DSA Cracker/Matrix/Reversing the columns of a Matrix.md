# Reversing the columns of a Matrix
**Problem Statement:**
Given an n×m matrix, reverse the order of columns in each row. This means the first column becomes the last, second becomes second-last, and so on. For each row, we need to swap elements symmetrically around the center. The solution involves iterating through each row and swapping elements at positions (i, j) with elements at positions (i, m-1-j) for j from 0 to m/2-1. Time complexity is O(n×m) and space complexity is O(1) as we perform in-place swapping without using extra space.

```cpp
class Solution
{
    public:
    //Function to reverse the columns of a matrix.
    void reverseCol(vector<vector<int> > &matrix){
        // code here
        int n=matrix.size(),m=matrix[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m/2;j++){
                swap(matrix[i][j],matrix[i][m-j-1]);
            }
        }
    }
};
```