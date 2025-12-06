# bfs path

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