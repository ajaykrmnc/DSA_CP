# Dijkstra’s

There are n cities and m flight connections between them. Your task is to determine the length of the shortest route
from Syrjälä to every cit

```cpp

int32_t main()
{
  speed()
  int n,m;
  cin>>n>>m;
  vector<vector<pair<int,int>>>adj(n+1);
  for(int i=0;i<m;i++){
    int a,b,w;
    cin>>a>>b>>w;
    adj[a].pb({b,w});
  }
  vector<int>d(n+1,LLONG_MAX),p(n+1,-1);
  int s=1;
  d[s] = 0;
  vector<int>vis(n+1,0);
  using pii = pair<int, int>;
  priority_queue<pii, vector<pii>, greater<pii>> q;
  q.push({0, s});
  while (!q.empty()) {
    int v = q.top().second;
    int d_v = q.top().first;
    q.pop();
    if(vis[v])continue;
    vis[v]=true;
    for (auto edge : adj[v]) {
      int to = edge.first;
      int len = edge.second;

      if (d[v] + len < d[to]) {
        d[to] = d[v] + len;
        p[to] = v;
        q.push({d[to], to});
      }
    }
  }
  for(int i=1;i<=n;i++){
    cout<<d[i]<<" ";
  }


  return 0;
}
```

