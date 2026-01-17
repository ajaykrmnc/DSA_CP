# No of components

**Problem Statement:**
Given an undirected graph with n nodes and m edges, find the number of connected components and output the minimum number of edges needed to make the graph connected. A connected component is a maximal set of nodes where there's a path between any two nodes. Use DFS or BFS to find all connected components. To make the graph connected, you need to add (number of components - 1) edges. The solution involves graph traversal to identify separate components and then connecting them optimally.

URL: https://cses.fi/problemset/task/1666

```cpp
int32_t main()
{
    speed();
    int n,m;
    cin>>n>>m;
    vector<vector<int>>adj(n+1);
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    queue <int> q;
    vector <int> dis;
    vector <int> vis(n+1,0);
    for(int i=1;i<=n;i++){  
        if(!vis[i]){    
            vis[i]=true;
            dis.push_back(i);
            q.push(i);
            while(!q.empty()){
                int node=q.front();
                q.pop();
                for(auto x: adj[node]){
                    if(!vis[x]){
                        vis[x]=true;
                        q.push(x);
                    }
                }
            }
        }
    }
    cout<<dis.size()-1<<nline;
    for(int i=0;i<dis.size()-1;i++){
         cout<<dis[i]<<" "<<dis[i+1]<<nline;
    }
 
    return 0;
}
```

[](https://gist.githubusercontent.com/ajaykrmnc/b5c3bcff7aff9e044e26b09185c58c22/raw/9328c82592b8df69a3b0613fac1e86f876ecfa4e/hello.cpp)