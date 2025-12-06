# Breaking good

problem link: https://codeforces.com/contest/507/problem/E

```cpp
struct tri{
    int a,b,c;
};
int32_t main()
{
    speed()
    int n;
    cin>>n;
    int m;
    cin>>m;
    vector<vector<pair<int,int>>>adj(n+1);
    map<pair<int,int>,int>mp;
    for(int i=0;i<m;i++){
        int a,b,c;
        cin>>a>>b>>c;
        adj[a].pb({b,c});
        adj[b].pb({a,c});
        mp[{a,b}]=c;
        mp[{b,a}]=c;
    }
    vector<int>vis(n+1,0);
    vector<pair<int,int>>cd(n+1);
    queue<int>q;
    q.push(1);
    vis[1]=1;
    cd[1]={0,0};
    vector<int>par(n+1);
    par[1]=-1;
    while(!q.empty()){
        int v=q.front();
        q.pop();
        for(auto [to,z]:adj[v]){
            if(!vis[to]){
                vis[to]=1;
                auto [x,y]=cd[v];
                if(z==1){
                    cd[to]={x+1,y+1};
                }else {
                    cd[to]={x,y+1};
                }
                par[to]=v;
                q.push(to);
            }else {
                auto [x,y]=cd[v];
                auto [a,b]=cd[to];
                if(y+1==b&&a<=x){
                    if(z==1){
                        cd[to]={x+1,b};
                    }else {
                        cd[to]={x,b};
                    }
                    par[to]=v;
                }
            }
        }
    }
    vector<tri>ans;
    map<pair<int,int>,int>mp2;
    for(int v=n;par[v]!=-1;v=par[v]){
        if(mp[{v,par[v]}]==0){
            ans.pb({v,par[v],1});
        }else{
            mp2[{v,par[v]}]=1;
        }
    }
    for(auto [x,y]: mp){
        if(y==0)continue;
        auto [u,v]=x;
        if(mp2[{u,v}]==0&&mp2[{v,u}]==0){
            ans.pb({u,v,0});
            mp2[{u,v}]=1;
        }
    }
    cout<<ans.size()<<nline;
    for(auto x: ans){
        auto [a,b,c]=x;
        cout<<a<<' '<<b<<' '<<c<<nline;
    }
    
    return 0;
}
```