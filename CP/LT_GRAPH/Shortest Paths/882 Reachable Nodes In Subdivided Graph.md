# 882. Reachable Nodes In Subdivided Graph

You are given an undirected graph (the **"original graph"**) with `n` nodes labeled from `0` to `n - 1`. You decide
to **subdivide** each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of `edges` where `edges[i] = [ui, vi, cnti]` indicates that there is an edge between
nodes `ui` and `vi` in the original graph, and `cnti` is the total number of new nodes that you will **subdivide** the
edge into. Note that `cnti == 0` means you will not subdivide the edge.

To **subdivide** the edge `[ui, vi]`, replace it with `(cnti + 1)` new edges and `cnti` new nodes. The new nodes
are `x1`, `x2`, ..., `xcnti`, and the new edges are `[ui, x1]`, `[x1, x2]`, `[x2, x3]`, ..., `[xcnti-1, 
xcnti]`, `[xcnti, vi]`.

In this **new graph**, you want to know how many nodes are **reachable** from the node `0`, where a node
is **reachable** if the distance is `maxMoves` or less.

Given the original graph and `maxMoves`, return *the number of nodes that are **reachable** from node* `0` *in the new
graph*.

**Example 1:**

```
Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13
Explanation: The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.

```

```cpp
class Solution {
public:
  int reachableNodes(vector<vector<int>>& edges, int maxMoves, int n) {
    vector<vector<pair<int,int>>>adj(n);
    for(auto v: edges){
      int to = v[0],from = v[1];
      adj[to].push_back({from,v[2] + 1});
      adj[from].push_back({to,v[2] + 1});
    }
    using pii = pair<int,int>;
    priority_queue<pii,vector<pii>,greater<pii>>q;
    const int inf = 1e9 + 7;
    vector <int>dist(n,inf);
    dist[0] = 0;
    q.push({0,0});
    while(q.size()){
      auto [len,top] = q.top();
      q.pop();
      for(auto [node,w]: adj[top]){
        if(dist[node] > dist[top] + w){
          dist[node] = dist[top] + w;
          q.push({dist[node],node});
        }
      }
    }
    int cnt = 0;
    for(int i = 0; i < n; i++){
      if(dist[i] <= maxMoves){
        cnt++;
      }
    }
    for(auto edge: edges){
      int num = 0,num2 = 0;
      if(dist[edge[1]] < maxMoves){
        num += min({maxMoves - dist[edge[1]],edge[2]});
      }
      if(dist[edge[0]] < maxMoves){
        num2 += min({maxMoves - dist[edge[0]],edge[2]});
      }
      cnt += min(num + num2, edge[2]);
    }
    return cnt;
  }
};
```
