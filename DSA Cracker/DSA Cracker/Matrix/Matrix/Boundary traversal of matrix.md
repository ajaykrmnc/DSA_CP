# Boundary traversal of matrix

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