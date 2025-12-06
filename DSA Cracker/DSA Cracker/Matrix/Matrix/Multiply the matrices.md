# Multiply the matrices

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