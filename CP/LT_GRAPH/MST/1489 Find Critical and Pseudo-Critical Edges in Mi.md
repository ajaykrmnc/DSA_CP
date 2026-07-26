# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

Given a weighted undirected connected graph with `n` vertices numbered from `0` to `n - 1`, and an
array `edges` where `edges[i] = [ai, bi, weighti]` represents a bidirectional and weighted edge between
nodes `ai` and `bi`. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without
cycles and with the minimum possible total edge weight.

Find *all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST)*. An MST edge whose
deletion from the graph would cause the MST weight to increase is called a *critical edge*. On the other hand, a
pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

**Example 1:**

```
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first
list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to
the second list of the output.
```

```cpp
bool sort_by_sec(const vector<int>&a, const vector<int>&b){
  return a[2] < b[2];
}
class Solution{
public:
  int find_parent(int u,vector<int>&parent){
    if(u == parent[u])
      return u;
    return find_parent(parent[u],parent);
  }
  void union1(int u,int v,vector<int>&parent){
    int pu = find_parent(u,parent);
    int pv = find_parent(v,parent);
    if(pu != pv){
      parent[pu] = pv;
    }
  }
  int MST(vector<vector<int>>&edges,int n,vector<int>&include,vector<int>&exclude){
    vector<int>parent(n);
    int calc_edes = 0;
    for(int i = 0; i < n; i++){
      parent[i] =i;
    }
    int cost = 0;
    if(include.size() != 0){
      int pu = find_parent(include[0],parent);
      int pv = find_parent(include[1],parent);
      union1(pu,pv,parent);
      cost+=include[2];
      calc_edes += 1;
    }
    for(auto it: edges){
      if(include.size() != 0 and it == include)continue;
      if(exclude.size() != 0 and it == exclude)continue;
      int pu = find_parent(it[0],parent);
      int pv = find_parent(it[1],parent);
      if(pu != pv){
        union1(pu,pv,parent);
        cost+=it[2];
        calc_edes += 1;
      }
    }
    return calc_edes == n - 1 ? cost : INT_MAX;
  }
  vector<vector<int>>findCriticalAndPseudoCriticalEdges(int n,vector<vector<int>>&edges){
    vector<vector<int>>originalEdges;
    for(auto edge: edges){
      vector<int>originalEdge{edge[0],edge[1],edge[2]};
      originalEdges.push_back(originalEdge);
    }
    sort(edges.begin(),edges.end(),sort_by_sec);
    vector<vector<int>>ans;
    vector<int>temp;
    int mst = MST(edges,n,temp,temp);
    vector<int>critical;
    vector<int> pseudocritical;
    for(int i = 0; i < edges.size(); i++){
      int exclude_cost = MST(edges,n,temp,originalEdges[i]);
      int include_cost = MST(edges,n,originalEdges[i],temp);
      if(exclude_cost > mst){
        critical.push_back(i);
      }else if(include_cost == mst){
        pseudocritical.push_back(i);
      }
    }
    ans.push_back(critical);
    ans.push_back(pseudocritical);
    return ans;
  }
};
```
