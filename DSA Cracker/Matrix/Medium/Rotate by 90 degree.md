# Rotate by 90 degree

**Problem Statement:**
Given a square matrix, rotate it by 90 degrees anticlockwise (or clockwise, depending on the problem variant). This transformation changes the position of each element: the element at position (i, j) moves to position (j, n-1-i) for clockwise rotation, or (n-1-j, i) for anticlockwise rotation. The rotation can be performed in-place using matrix transposition followed by row/column reversal, or by using a temporary matrix. The in-place approach is more space-efficient with O(1) extra space, while the temporary matrix approach is more intuitive but uses O(n²) extra space.

```cpp
class Solution
{   
    public:
    //Function to rotate matrix anticlockwise by 90 degrees.
    void rotateby90(vector<vector<int> >& matrix, int n) 
    { 
        // code here 
        for(int i = 0; i < n; i++){
            reverse(matrix[i].begin(), matrix[i].end());
        }
        
        //transposing the matrix
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < i; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    } 
};
```