# interchanging the rows of a Matrix

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