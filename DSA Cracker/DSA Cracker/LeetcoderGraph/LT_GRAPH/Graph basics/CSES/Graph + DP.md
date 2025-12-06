# Graph + DP

URL: https://cses.fi/problemset/task/1195

Your task is to find a minimum-price flight route from Syrjälä to Metsälä. You have one discount coupon, using which you can halve the price of any single flight during the route. However, you can only use the coupon once.

When you use the discount coupon for a flight whose price is x, its price becomes ⌊x/2⌋ (it is rounded down to an integer)

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
    int dp[n+1][2];
    for(int i=0;i<n+1;i++){
        for(int j=0;j<2;j++){
            dp[i][j]=LLONG_MAX;
        }
    }
    int s=1;
    dp[s][0] = 0;
    dp[s][1] = 0;
    vector<vector<int>>vis(n+1,vector<int>(2,0));
    using pii = pair<int, pair<int,int>>;
    priority_queue<pii, vector<pii>, greater<pii>> q;
    q.push({0, {s,0}});
    q.push({0, {s,1}});
    while (!q.empty()) {
        auto [len,z]=q.top();
        auto [v,flag]=z;
        q.pop();
        if(flag==1&&vis[v][1]==1){
            continue;
        }else if(flag==0&&vis[v][0]==1){
            continue;
        }
        vis[v][flag]=1;
        for (auto [to,len] : adj[v]) {
            if(flag==0){
                if(dp[to][0]>dp[v][0]+len){
                    dp[to][0]=dp[v][0]+len;
                    q.push({dp[to][0],{to,0}});
                }
                if(dp[to][1]>dp[v][0]+len/2){
                    dp[to][1]=dp[v][0]+len/2;
                    q.push({dp[to][1],{to,1}});
                }
            }else {
                if(dp[to][1]>dp[v][1]+len){
                    dp[to][1]=dp[v][1]+len;
                    q.push({dp[to][1],{to,1}});
                }
            }
        }
    }
    cout<<min(dp[n][1],dp[n][0])<<nline;
 
    return 0;
}
```