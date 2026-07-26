# way to reach in directed graph

Tags: kahn
URL: https://cses.fi/problemset/task/1681

A game has n levels, connected by m teleporters, and your task is to get from level 1 to level n. The game has been designed so that there are no directed cycles in the underlying graph. In how many ways can you complete the game?

# Input

```cpp
int32_t main()
{
    speed()
    int n,m;
    cin>>n>>m;
    vector<vector<int>>adj(n+1);
    vector<int>indeg(n+1,0);
    vector<int>dp(n+1,0);
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        adj[a].pb({b});
        indeg[b]++;
    }
    using pii=pair<int,int>;
    queue<int>q;
    for(int i=0;i<n+1;i++){
        if(indeg[i]==0){
            q.push(i);
        }
    }
    vector<int>ans;
    vector<int>vis(n+1,0);
    dp[1]=1;
    while(!q.empty()){
         int node=q.front();
         q.pop();
         ans.pb(node);
         for(auto x: adj[node]){
            indeg[x]--;
            if(indeg[x]==0){
                q.push(x);
            }
            dp[x]+=dp[node];
            dp[x]%=mod;
         }
    }
    cout<<dp[n]<<nline;
    return 0;
}
```