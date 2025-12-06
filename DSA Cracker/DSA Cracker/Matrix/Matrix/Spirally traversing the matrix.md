# Spirally traversing the matrix

```cpp
class Solution
{   
    public: 
    //Function to return a list of integers denoting spiral traversal of matrix.
    vector<int> spirallyTraverse(vector<vector<int> > matrix, int r, int c) 
    {
        // code here 
        // boundary traversal of matrix
        vector<int>ans;
        int left=0,right=c,top=0,bottom=r;
        while(left<right and top<bottom){
            for(int i=left;i<right;i++){
                ans.push_back(matrix[top][i]);
            }
            for(int j=top+1;j<bottom-1;j++){
                ans.push_back(matrix[j][right-1]);
            }
            for(int i=right-1;i>=left and top+1<bottom ;i--){
                ans.push_back(matrix[bottom-1][i]);
            }
            for(int j=bottom-2;j>top and left+1<right ;j--){
                ans.push_back(matrix[j][left]);
            }
            top++;
            bottom--;
            left++;
            right--;
        }
        return ans;
    }
};
```