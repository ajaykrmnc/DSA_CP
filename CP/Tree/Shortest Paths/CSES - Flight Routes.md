# CSES - Flight Routes

URL: https://cses.fi/problemset/task/1196

Your task is to find the k shortest flight routes from Syrjälä to Metsälä. A route can visit the same city several times.

Note that there can be several routes with the same price and each of them should be considered (see the example).

```cpp
class solve{
public:
solve(){
    int n,m;
    cin>>n>>m;
    int k;
    cin>>k;
    vector<vector<pair<int,int>>>adj(n+1);
    for(int i=0;i<m;i++){
        int a,b,c;
        cin>>a>>b>>c;
        adj[a].pb({b,c});
    }
    using pii=pair<int,int>;
    vector<vector<int>>dp(n+1);
    priority_queue<pii,vector<pii>,greater<pii>>pq;
    priority_queue<int>bes[n+1];
    dp[1].pb(0);
    vector<int>vis(n+1,0);
    vector<int>d(n+1,inf);
    d[1]=0;
    bes[1].push(0); pq.push({0,1});
    while(!pq.empty()){
        auto [w,u]=pq.top();
        pq.pop();
        if (w > bes[u].top()) continue;
        for(auto [to,len]: adj[u]){
           int tmp= w+len;
           if(bes[to].size()<k){
             bes[to].push(tmp);
             pq.push({tmp,to});
           }else if(tmp<bes[to].top()){
                bes[to].pop();
                bes[to].push(tmp);
                pq.push({tmp,to});
           }
    
    }
    }
    vector<int>ans;
    while(!bes[n].empty()){
        ans.pb(bes[n].top());
        bes[n].pop();
    }
    reverse(all(ans));
    for(auto x: ans){
        cout<<x<<' ';
    }
}
```