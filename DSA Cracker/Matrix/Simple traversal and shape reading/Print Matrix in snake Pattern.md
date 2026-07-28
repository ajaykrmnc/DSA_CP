# Print Matrix in snake Pattern

**Problem Statement:**
Given an n×m matrix, print the elements in snake pattern. In snake pattern, we traverse the first row from left to right, second row from right to left, third row from left to right, and so on, alternating the direction for each row. This creates a snake-like traversal pattern. Use a flag to keep track of the current direction - when flag is 0, traverse left to right; when flag is 1, traverse right to left. Toggle the flag after each row. Time complexity is O(n×m) and space complexity is O(1) excluding the result array.

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