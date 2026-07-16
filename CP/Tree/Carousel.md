# Carousel

**Problem Statement:**
You have a circular carousel with n seats arranged in a circle, where each seat has a type t[i]. You need to color the seats
such that no two adjacent seats of the same type have the same color. Find the minimum number of colors needed and assign
colors to each seat. This is a graph coloring problem where you create edges between adjacent seats of different types,
then use DFS to assign colors. The solution involves building a graph, performing DFS traversal, and handling conflicts
when adjacent seats of the same type need different colors.

problem link: https://codeforces.com/contest/1328/problem/D

```cpp
using vb = vector<bool>;
using vvb = vector<vb>;
using vi = vector<int>;
using vvi = vector<vi>;
using vl = vector<ll>;
using vvl = vector<vl>;
int n = 2e5 + 5;
vvi adj(n);
vb vis(n);
vi col(n,-1);

void dfs(int u)
{
    vis[u] = 1;
    for (int v:adj[u]){
        if (col[v] == col[u]){//discrepancy
            col[u] = 3;//we can also set col[v] = 3
            continue;
        }
        if (!vis[v]){
            if (col[u] == 1)col[v] = 2;
            else if (col[u] == 2)col[v] = 1;
            else col[v] = 1;//else col[u] == 3 hence set col[v] to be 1 or 2
            dfs(v);
        }
    }
}
void createGraph()
{
    cin>>n;
    for (int i = 1;i<=n;i++)adj[i].clear(),vis[i] = 0,col[i] = -1;
    vi t(n + 1);
    for (int i = 1;i<=n;i++)cin>>t[i];

    for (int i = 1;i<n;i++){
            if (t[i] != t[i + 1]){
            adj[i].pb(i + 1),adj[i + 1].pb(i);//because the graph is undirected
        }
    }

    if (t[1] != t[n]){
        adj[1].pb(n);
        adj[n].pb(1);
    }

    for (int i = 1;i<=n;i++){
        if (!vis[i]){
            col[i] = 1;//the colours are 1,2 or 3
            dfs(i);
        }
    }
    //output the # of colours
    int ans = 1;
    for (int i = 1;i<=n;i++)ans = max(ans,col[i]);//find the max colour # used
    cout<<ans<<'\n';
    for (int i = 1;i<=n;i++)cout<<col[i]<<" ";
    cout<<'\n';
}
int main()
{
    setIO();
    int t;
    cin>>t;
    while (t--){
        createGraph();
    }
    return 0;
}
```

