# Modify Graph Edge Weight

problem link: https://leetcode.com/problems/modify-graph-edge-weights/description/

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
