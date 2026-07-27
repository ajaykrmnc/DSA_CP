# Bicycles

**Problem Statement:**
You have a graph with n cities and m roads. Each city has bicycles with different slowness factors. You start at city 1
and want to reach city n in minimum time. At each city, you can switch to a bicycle with a different slowness factor.
The time to travel on a road equals road_length \* current_bicycle_slowness. This is a shortest path problem with state
(city, bicycle_type). Use Dijkstra's algorithm with states representing both current city and current bicycle. The key
insight is that you might want to take a longer path to get a faster bicycle for future roads.

[Problem - G - Codeforces](https://codeforces.com/contest/1915/problem/G)

```cpp
int main(){
  int tt = scd();
  while(tt--) {
    int n = scd(), m = scd();
    vector<vector<array<int, 2>>> G(n + 1);
    repI(i, 1, m) {
      int u = scd(), v = scd(), w = scd();
      G[u].push_back({v, w});
      G[v].push_back({u, w});
    }
    vector<lld> Slowness(n + 1, 0);
    repI(i, 1, n) {
      Slowness[i] = sc();
    }
    vector<vector<lld>> dist(n + 1, vector<lld>(1005, 1e18));
    dist[1][Slowness[1]] = 0;
    priority_queue<array<lld, 3>, vector<array<lld, 3>>, greater<array<lld, 3>>> pq;
    pq.push({0, 1, Slowness[1]});
    while(!pq.empty()) {
      array<lld, 3> top = pq.top();
      pq.pop();
      lld d = top[0], u = top[1], s = top[2];
      if(d > dist[u][s]) continue;
      for(array<int, 2> v : G[u]) {
        lld newDist = dist[u][s] + v[1] * s;
        lld newSlowness = min(s, Slowness[v[0]]);
        if(newDist < dist[v[0]][newSlowness]) {
          dist[v[0]][newSlowness] = newDist;
          pq.push({newDist, v[0], newSlowness});
        }
      }
    }
    lld ans = 1e18;
    repI(i, 1, 1000) {
      ans = min(ans, dist[n][i]);
    }
    prL(ans);
  }
  return 0;
}
```

