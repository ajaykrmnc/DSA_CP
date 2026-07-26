# 684. Redundant Connection

In this problem, a tree is an **undirected graph** that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return *an edge that can be removed so that the resulting graph is a tree of* `n` *nodes*. If there are multiple answers, return the answer that occurs last in the input.

• `3 <= n <= 1000`

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg)

```cpp
class Solution {
    bool dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& vis) {
        vis[node] = true;
        for(auto it : adj[node]) {
            if(!vis[it]){
                if(dfs(it, node, adj, vis)) return true;
            }else if(it!=parent) return true;
        }
        return false;
    }
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edge) {
        int n = edge.size();
        vector<vector<int>> adj(n+1);
        vector<bool> vis(n+1, 0);                
        for(auto i : edge) {
            fill(begin(vis), end(vis), 0);
            adj[i[0]].push_back(i[1]);
            adj[i[1]].push_back(i[0]);
            if(dfs(i[0], -1, adj, vis)) return i;
        }
        return {};
    }

};
```

```cpp
By DSU

class Solution {
public:
    int parent[1001] = {0};
    int findParent(int x) {
      if(x==parent[x]) {
        return x;
      }
      return parent[x] = findParent(parent[x]);
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        for(int i=0;i<=1000;i++) {
          parent[i] = i;
        }
        vector<int> ans;
        for(int i=0;i<edges.size();i++) {
          int u = findParent(edges[i][0]);
          int v = findParent(edges[i][1]);
          if(u==v) {
            ans.push_back(edges[i][0]);
            ans.push_back(edges[i][1]);
            return ans;
          } else {
            parent[v] = u;
          }
        }
        return ans;
    }
};
```