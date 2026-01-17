# Solve the Sudoku

**Problem Statement:**
Given an incomplete 9×9 Sudoku grid, fill the empty cells to complete the puzzle. Use backtracking algorithm to try different
numbers (1-9) in empty cells, checking if the placement is valid according to Sudoku rules. If a placement leads to a dead end,
backtrack and try the next possibility. The algorithm recursively explores all possibilities until a solution is found.
Time complexity is exponential in worst case but pruning makes it practical. This problem demonstrates the power of backtracking
for constraint satisfaction problems.

Given an incomplete [**Sudoku**](https://en.wikipedia.org/wiki/Sudoku) configuration in terms of a 9 x 9  2-D square matrix (grid[][]), the task is to find a solved Sudoku. For simplicity, you may assume that there will be only one unique solution.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

Zeros in the grid indicates blanks, which are to be filled with some number between 1-9. You can not replace the element in the cell which is not blank.

```cpp
class Solution 
{
    public:
    //Function to find a solved Sudoku. 
    
    bool isValid(int grid[N][N],int row,int col,int val){
        for(int i=0;i<N;i++){
            if(grid[i][col]== val){
                return false;
            }
            if(grid[row][i]== val){
                return false;
            }
            if(grid[3*(row/3)+i/3][3*(col/3)+i%3]==val){
                return false;
            }
        }
        return true;
    }
    bool solve(int grid[N][N])  
    { 
        // Your code here
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(grid[i][j]==0){
                    for(int c=1;c<=9;c++){
                        if(isValid(grid,i,j,c)){
                            grid[i][j] = c;
                            if(solve(grid)) return true;
                            else grid[i][j] = 0;
                        }
                    }
                    return false;
                }
            }
        }
    }
    bool SolveSudoku(int grid[N][N]){
        return solve(grid);
    }
    
    //Function to print grids of the Sudoku.
    void printGrid (int grid[N][N]) 
    {
        // Your code here 
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                cout<<grid[i][j]<<' ';
            }
        }
    }
};
```