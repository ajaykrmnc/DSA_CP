# Add two matrix

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