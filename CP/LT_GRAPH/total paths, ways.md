# total paths, ways
**Problem Statement:**
Find the shortest path from city 1 to city n and answer 4 queries: minimum cost, number of minimum-cost routes (mod 10^9+7), minimum flights in shortest route, maximum flights in shortest route. Use modified Dijkstra's algorithm with additional state tracking. For each node, maintain: distance, number of ways to reach with minimum distance, minimum and maximum number of edges in shortest paths. When relaxing edges, update all these values appropriately. This combines shortest path algorithms with counting and optimization problems.

URL: https://cses.fi/problemset/task/1202

You are going to travel from Syrjälä to Lehmälä by plane. You would like to find answers to the following questions:

- what is the minimum price of such a route?
- how many minimum-price routes are there? (modulo 109+7)

    109+7)10^9+7)

- what is the minimum number of flights in a minimum-price route?
- what is the maximum number of flights in a minimum-price route?

# Output

Print four integers according to the problem statement.

# Example

Input:

```
4 5
1 4 5
1 2 4
2 4 5
1 3 2
3 4 3

```

Output:

```
5 2 1 2
```

```cpp
#include <bits/stdc++.h>
using namespace std;

const int inf=LLONG_MAX;
const int mod=1e9+7;
struct node{
    int ways,mini,maxi;
};
int32_t main()
{
    speed()
    int n,m;
    cin>>n>>m;
    using pii=pair<int,int>;
    vector<vector<pii>>adj(n+1);
    for(int i=0;i<m;i++){
        int a,b,c;
        cin>>a>>b>>c;
        adj[a].pb({b,c});
    }
    priority_queue<pii,vector<pii>,greater<pii>>pq;
    vector<int>d(n+1,inf);
    d[1]=0;
    vector<node>infor(n+1,{0,inf,0});
    pq.push({0,1});
    infor[1]={1,0,0};
    vector<int>vis(n+1,0);
    while(!pq.empty()){
        auto [w,u]=pq.top();
        pq.pop();
        if(vis[u])continue;
        vis[u]=true;
        for(auto [to,len]: adj[u]){
            auto [x,y,z]=infor[u];
            auto [j,k,l]=infor[to]; // {ways, min, max}
            if(d[u]+len==d[to]){
                j+=x;
                j%=mod;
                k=min(y+1,k);
                l=max(z+1,l);
                infor[to]={j,k,l};
            }
            else if(d[u]+len<d[to]){
                d[to]=d[u]+len;
                j=x;
                k=y+1;
                l=z+1;
                infor[to]={j,k,l};
                pq.push({d[to],to});
            }
        }
    }
    auto [x,y,z]=infor[n];
    cout<<d[n]<<' '<<x<<' '<<y<<' '<<z<<nline;

    return 0;
}
```