# Gardener and tree

```cpp
bool solve()
{
    ll n,k,ans=0,ops=0;
    cin >> n >> k;
 
    vector<set<ll>> adj(n);
    vector<ll> vis(n,0);
 
    for(ll i=1,x,y ; i<n ; ++i)
    {
        cin >> x >> y;
        x--,y--;
 
        adj[x].insert(y);
        adj[y].insert(x);
    }
 
    vector<ll> now;
 
    for(ll i=0 ; i<n ; ++i)
    {
        if(adj[i].size()<=1){
            deb(i);
            vis[i] = 1;
            now.pb(i);
        }
    }
 
    while(ans<n && ops<k)
    {
        vector<ll> next;
        for(auto curr : now){   
            ans++;
 
            for(auto x : adj[curr])
            {
                if(!vis[x])
                {
                    adj[x].erase(curr);
                    if(adj[x].size()<=1)
                    {
                        vis[x] = 1;
                        next.pb(x);
                    }
                }
            }
        }
            
        deb(ans,next);
 
        now = next;
 
        ops++;
    }
 
    cout << n-ans << endl;
    return true;    
}
```