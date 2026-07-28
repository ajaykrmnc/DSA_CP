# Transpose of a matrix

**Problem Statement:**
Given a square matrix, find its transpose. The transpose of a matrix is obtained by swapping rows and columns, i.e.,
the element at position (i, j) becomes the element at position (j, i). For a square matrix, this can be done in-place
by swapping elements across the main diagonal. The algorithm iterates through the upper triangle of the matrix and swaps
each element with its corresponding element across the diagonal. Time complexity is O(n²) and space complexity is O(1)
for in-place transposition. This operation is fundamental in linear algebra and matrix computations.

```cpp
class Solution
{   
    public:  
    //Function to find transpose of a matrix.
    void transpose(vector<vector<int> >& matrix, int n)
    { 
        // code here 
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                swap(matrix[i][j],matrix[j][i]);
            }
        }
    }
};
```