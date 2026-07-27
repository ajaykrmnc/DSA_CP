# Directed Graph Bellman Ford

**Problem Statement:**
You play a game consisting of n rooms and m tunnels. Your initial score is 0, and each tunnel increases your score by x
where x may be both positive or negative. You may go through a tunnel several times. Your task is to walk from room 1 to
room n and find the maximum score you can get.

This is a longest path problem in a directed graph with possible cycles. Use modified Bellman-Ford algorithm to detect
positive cycles and find maximum distances. Handle infinite score cases carefully.

URL: [Link](https://cses.fi/problemset/task/1673)

```cpp
const int INF=LLONG_MAX;

struct edge{
  int a, b, cost;
};

int n,m;
vector<edge>e;
vector<vector<int>>adj;
vector<int>vis;
vector<int>d;

void dfs(int node){
  vis[node]=1;
  for(auto u: adj[node]){
    if(!vis[u]){
      dfs(u);
    }
  }
}
void solve(){
  d[1] = 0;
  for (int i=0; i<n-1; ++i)
    for (int j=0; j<m; ++j)
      if (d[e[j].a] != -INF)
        d[e[j].b] = max (d[e[j].b], d[e[j].a] + e[j].cost);
}

int32_t main() {
  cin>>n>>m;
  e.resize(m);
  adj.resize(n+1);
  vis.resize(n+1,0);
  d.resize(n+1,-INF);
  for(int i=0;i<m;i++){
    int a,b,c;
    cin>>a>>b>>c;
    e[i]={a,b,c};
    adj[a].pb(b);
  }
  solve();
  for(int i=0;i<m;i++){
    if(d[e[i].a]!=-INF && d[e[i].b]<d[e[i].a]+e[i].cost){
      dfs(e[i].a);
    }
  }
  if(!vis[n]){
    cout<<d[n]<<nline;
  }else
  cout<<-1<<nline;


  return 0;
}
```
