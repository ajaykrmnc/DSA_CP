# M-Coloring Problems

Given an undirected graph and an integer **M**. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

**Example 1:**

```cpp
class Solution{
public:
    // Function to determine if graph can be coloured with at most M colours such
    // that no two adjacent vertices of graph are coloured with same colour.
    bool isSafe(int node,vector<int>&color,bool graph[101][101],int n,int col){
        for(int k=0;k<n;k++){
            if(k!=node and graph[k][node]==1 and color[k]==col){
                return false;
            }
        }
        return true;
    }
    bool solve(int node,vector<int>&color,int m,int n,bool graph[101][101]){
        if(node==n){
            return true;
        }
        for(int i=1;i<=m;i++){
            if(isSafe(node,color,graph,n,i)){
                color[node]=i;
                if(solve(node+1,color,m,n,graph)){
                    return true;
                }
                // backtrack
                color[node]=0;
            }
        }
        return false;
    }
    
    bool graphColoring(bool graph[101][101], int m, int n) {
        // your code here
        vector<int>color(n,0);
        if(solve(0,color,m,n,graph)){
            return true;
        }
        
        return false;
    }
};
```