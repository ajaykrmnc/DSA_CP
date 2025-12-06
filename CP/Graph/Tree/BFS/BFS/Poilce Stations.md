# Poilce Stations

problem link: https://codeforces.com/problemset/problem/796/D

```cpp

int32_t main()
{
    speed()
    int n,k,d;
    cin>>n>>k>>d;
    vector<vector<int>>adj(n+1);
    set<int>st;
    for(int i=0;i<k;i++){
        int a;cin>>a;
        st.insert(a);
    }
    vector<pair<int,int>>pii(n+1);
    mac(i,0,n-1){
        int a,b;
        cin>>a>>b;
        adj[a].pb(b);
        adj[b].pb(a);
        pii[i]={a,b};
    }
    vector<int>vis(n+1,0);
    vector<int>purvaj(n+1);
    queue<int>q;
    for(auto x:st){
        q.push(x);
        vis[x]=1;
        purvaj[x]=x;
    }
    while(!q.empty()){
        int node=q.front();
        q.pop();
        for(auto x: adj[node]){
            if(!vis[x]){
                vis[x] = 1;
                q.push(x);
                purvaj[x] = purvaj[node];
            }
        }
    }
    vector<int>ans;
    for(int i=0;i<pii.size();i++){
        auto [a,b]=pii[i];
        if(purvaj[a] != purvaj[b]){
            ans.pb(i+1);
        }
    }
    cout<<ans.size()<<nline;
    for(auto x: ans){
        cout<<x<<" ";
    }

    return 0;
}
```