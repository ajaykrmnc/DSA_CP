# bfs path

**Problem Statement:**
Given an undirected graph with n nodes and m edges, find the shortest path from node 1 to node n. If no path exists,
print "IMPOSSIBLE". Otherwise, print the length of the shortest path and the path itself. This is a classic BFS problem
where we need to find the shortest path in an unweighted graph. Use BFS to explore nodes level by level, maintaining
parent pointers to reconstruct the path. The BFS guarantees that the first time we reach node n, we have found the
shortest path. Time complexity is O(n + m).

URL: https://cses.fi/problemset/task/1667/

```cpp
solve(){
  int n,m;
  cin>>n>>m;
  vector<vector<int>>adj(n+1);
  for(int i=0;i<m;i++){
    int a,b;
    cin>>a>>b;
    adj[a].pb(b);
    adj[b].pb(a);
  }
  queue<int>q;
  q.push(1);
  vector<int>par(n+1,-1);
  vector<int>vis(n+1,0);
  vis[1]=true;
  while(!q.empty()){
    int node=q.front();
    q.pop();
    for(auto x: adj[node]){
      if(!vis[x]){
        vis[x]=true;
        par[x]=node;
        q.push(x);
      }
    }
  }
  if(!vis[n]){
    cout<<"IMPOSSIBLE"<<nline;
    return 0;
  }else{
    vector<int>path;
    for(int v=n;v!=-1;v=par[v]){
      path.push_back(v);
    }
    reverse(all(path));
    cout<<path.size()<<nline;
    for(auto x: path){
      cout<<x<<' ';
    }
    cout<<nline;
  }

  return 0;
}
```

