# Multiply the matrices

**Problem Statement:**
Given two matrices A and B, multiply them to get the resultant matrix C. Matrix multiplication is possible only when the number of columns in matrix A equals the number of rows in matrix B. If A is of size p×q and B is of size q×r, then the resultant matrix C will be of size p×r. Each element C[i][j] is calculated as the dot product of the i-th row of A and j-th column of B. The time complexity is O(p×q×r). If matrices cannot be multiplied due to incompatible dimensions, return a matrix with -1.

```cpp
class Solution
{   
    public:
    //Function to multiply two matrices.
    vector<vector<int> > multiplyMatrix( const vector<vector<int> >& A, const vector<vector<int> >& B)
    {
        // code here
        if(A[0].size()!=B.size()){
            return vector<vector<int>>(1,vector<int>(1,-1));
        }
        int p=A.size(),q=A[0].size(),r=B[0].size();
        vector<vector<int>>ans(p,vector<int>(r,0));
        for(int i=0;i<p;i++){
            for(int j=0;j<r;j++){
                int sum=0;
                for(int k=0;k<q;k++){
                    sum+=A[i][k]*B[k][j];
                }
                ans[i][j]=sum;
            }
        }
        return ans;
    }
};
```