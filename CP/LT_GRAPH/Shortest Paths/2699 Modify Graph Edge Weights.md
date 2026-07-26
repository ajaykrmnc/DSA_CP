# 2699. Modify Graph Edge Weights

Tags: dijkstra's

You are given an **undirected weighted** **connected** graph containing `n` nodes labeled from `0` to `n - 1`, and an
integer array `edges` where `edges[i] = [ai, bi, wi]` indicates that there is an edge between nodes `ai` and `bi` with
weight `wi`.

Some edges have a weight of `-1` (`wi = -1`), while others have a **positive** weight (`wi > 0`).

Your task is to modify **all edges** with a weight of `-1` by assigning them **positive integer values** in the
range `[1, 2 * 109]` so that the **shortest distance** between the nodes `source` and `destination` becomes equal to an
integer `target`.

If there are **multiple** **modifications** that make the shortest distance
between `source` and `destination` equal to `target`, any of them will be considered correct.

Return *an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest
distance from* `source` *to* `destination` *equal to* `target`_, or an **empty array** if it's impossible._

**Note:** You are not allowed to modify the weights of edges with initial positive weights.

**Example 1:**

```
Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.
```

```cpp
class Solution {
public:
  vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int src, int dest, int target) {
    const long long inf = 2e9;
    vector<vector<pair<long long,long long>>>graph1(n),graph2(n);
    map<pair<long long,long long>,long long>mp;
    for(auto edge: edges){
      long long to = edge[0],from = edge[1],w = edge[2];
      if(to > from){
        swap(to,from);
      }
      mp[{to,from}] = w;
      if(w == -1){
        graph1[to].push_back({from,1});
        graph2[to].push_back({from,inf});
        graph1[from].push_back({to,1});
        graph2[from].push_back({to,inf});
      }else{
        graph1[to].push_back({from,w});
        graph2[to].push_back({from,w});
        graph1[from].push_back({to,w});
        graph2[from].push_back({to,w});
      }
    }
    vector<long long>par(n),init(n);
    auto dij = [&](vector<vector<pair<long long,long long>>>&graph){
      using pii = pair<long long,long long>;
      priority_queue<pii,vector<pii>,greater<pii>>pq;
      pq.push({0,src});
      vector<long long>dist(n,inf);
      dist[src] = 0;
      par[src] = -1;
      while(pq.size()){
        auto [len,top] = pq.top();
        pq.pop();
        for(auto [node,w]: graph[top]){
          if(dist[node] > dist[top] + w){
            par[node] = top;
            dist[node] = dist[top] + w;
            pq.push({dist[node],node});
          }
        }
      }
      return dist[dest];
    };
    long long mini =  dij(graph2); long long maxi = dij(graph1);
    cout << mini << " " << maxi << endl;
    if(mini == target){
      vector<vector<int>>ans = edges;
      for(auto &edge: ans){
        if(edge[2] == -1){
          edge[2] = inf;
        }
      }
      return ans;
    }  if(maxi > target or target > mini){
      return {};
    }
    init = par;
    int node = dest;
    for(int i = 0; i < n; i++){
      cout <<init[i] << ' ';
    }
    cout << endl;
    while(init[node] != -1){
      long long to = node;
      long long from = init[node];
      cout << to << ' ' << from << endl;
      if(to > from)
        swap(to,from);
      if(mp[{to,from}] == -1){
        mp[{to,from}] = 1;
      }else{
        node = init[node];
        continue;
      }
      for(auto &[child,len]: graph2[to]){
        if(child == from){
          len = mp[{to,from}];
        }
      }
      for(auto &[child,len]: graph2[from]){
        if(child == to){
          len = mp[{to,from}];
        }
      }
      int req = dij(graph2);
      if(req <= target){
        mp[{to,from}] = target - req + 1;
        break;
      }
      node = init[node];
    }
    vector<vector<int>>ans;
    for(auto edge: edges){
      int to = edge[0],from = edge[1];
      if(to > from){
        swap(to,from);
      }
      int res;
      if(mp[{to,from}] == -1){
        res = 2*(1e9);
      }else{
        res = mp[{to,from}];
      }
      ans.push_back({edge[0],edge[1],res});
    }
    return ans;
  }
};
```

