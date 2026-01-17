# Add two matrix

**Problem Statement:**
Given two matrices A and B of the same dimensions, add them element-wise to get the resultant matrix C. Matrix addition is only possible when both matrices have the same number of rows and columns. Each element C[i][j] = A[i][j] + B[i][j]. If the matrices have different dimensions, return a matrix containing -1 to indicate that addition is not possible. The time complexity is O(m×n) where m and n are the dimensions of the matrices. This is a fundamental matrix operation used in various mathematical computations.

```cpp
class Solution
{   
    public:
    //Function to add two matrices.
    vector<vector<int> > sumMatrix( const vector<vector<int> >& A, const vector<vector<int> >& B)
    {
        // code here
        if(A.size()!=B.size() || (A[0].size()!=B[0].size())){
            return vector<vector<int>>(1,vector<int>(1,-1));
        }
        vector<vector<int>>result(A.size());
        for(int i=0;i<A.size();i++){
            for(int j=0;j<A[0].size();j++){
                result[i].push_back(A[i][j]+B[i][j]);
            }
        }
        return result;
    }
};
```