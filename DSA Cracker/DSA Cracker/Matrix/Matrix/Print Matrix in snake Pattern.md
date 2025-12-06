# Print Matrix in snake Pattern

```cpp
class Solution
{   
    public:
    //Function to return list of integers visited in snake pattern in matrix.
    vector<int> snakePattern(vector<vector<int> > matrix)
    {   
        // code here
        int p = matrix[0].size();
        int flag=0;
        vector<int>ans;
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<p;j++){
                if(flag){
                    ans.push_back(matrix[i][p-j-1]);
                }else{
                    ans.push_back(matrix[i][j]);
                }
            }
            flag = 1-flag;
        }
        return ans;
    }
};
```