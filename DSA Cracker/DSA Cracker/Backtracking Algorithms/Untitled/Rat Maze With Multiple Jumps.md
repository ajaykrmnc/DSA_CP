# Rat Maze With Multiple Jumps

**Problem Statement:**
A maze is given as an N×N matrix where the rat starts at maze[0][0] and needs to reach maze[N-1][N-1]. The value at
maze[i][j] represents the maximum number of steps the rat can jump from that position. Use backtracking to explore all
possible paths: from each position, try jumping 1 to maze[i][j] steps in both right and down directions. If a path leads
to a dead end, backtrack and try alternative routes. Mark visited cells to avoid cycles and unmark them during backtracking.
This problem combines maze traversal with variable step sizes, making it more complex than standard rat maze problems.

A Maze is given as **N*N** matrix of blocks where source block is the upper left most block i.e., **maze[0][0]** and destination block is lower rightmost block i.e., **maze[N-1][N-1]**. Find if it is possible for the rat to reach from the source block to the destination block. The number of steps rat can jump from (i, j) is represented by maze[i][j].

**Note:**

```cpp
bool isSafe(int i,int j,vector<int>maze[],int N){
    if(i>=N or j>=N or maze[i][j]==0 )return false;
    return true;
}

bool utils(vector<vector<int>>&ans,vector<int>maze[],int N,int i,int j){
    if(i==N-1 and j==N-1){
        ans[i][j] = 1;
        return true;
    }
    if(isSafe(i, j, maze, N)){
        ans[i][j] = 1;
        for(int steps = 1;steps<= maze[i][j]; steps++){
            if(utils(ans,maze,N,i,j+steps)) return true;
            else if(utils(ans,maze,N,i+steps,j))return true;
        }
        // .. backtrack
        ans[i][j]=0;
    }
    return false;
}

//Function to find the minimum number of Hops required for the rat to 
//reach from the source block to the destination block. 
void solve(int N, vector<int> maze[]) 
{
    // write code here
    vector<vector<int>>ans(N,vector<int>(N,0));
    if(!utils(ans,maze,N,0,0)) cout<<-1 <<endl;
    else {
        for(int i=0;i<N;++i){
            for(int j=0;j<N;j++){
                cout<<ans[i][j]<<' ';
            }
            cout<<"\n";
        }
    }
    
}
```