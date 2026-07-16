# 886. Possible Bipartition

**Problem Statement:**
Given n people and a list of dislikes, determine if it's possible to split everyone into two groups such that people who
dislike each other are in different groups.

This is a classic bipartite graph problem. Model the dislikes as edges in a graph and check if the graph is bipartite
using DFS or BFS coloring. Try to color each person with one of two colors,
ensuring that adjacent people (who dislike each other) have different colors. If you can successfully color the entire
graph, then bipartition is possible.

Time complexity is O(V + E) and space complexity is O(V) for the color array.

Tags: bipartite

**Example 1:**

```
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
```

```cpp
class Solution {
public:
  bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
    vector<int>adj[n+1];
    vector<int>color(n+1,-1);
    for(int i = 0; i < dislikes.size(); ++i){
      int u = dislikes[i][0];
      int v = dislikes[i][1];
      adj[u].push_back(v);
      adj[v].push_back(u);
    }
    for(int i = 1; i <= n; ++i){
      if(color[i] == -1){
        if(!bipartiteDfs(i,adj,color)) return false;
      }
    }
    return true;
  }
  bool bipartiteDfs(int node,vector<int>adj[],vector<int>& color){

    for(auto& edges: adj[node]){
      if(color[edges] == -1){
        color[edges] = 1 - color[node];
        if(!bipartiteDfs(edges,adj,color)) return false;
      }
      else if(color[edges] == color[node]) return false;
    }
    return true;
  }
};
```

