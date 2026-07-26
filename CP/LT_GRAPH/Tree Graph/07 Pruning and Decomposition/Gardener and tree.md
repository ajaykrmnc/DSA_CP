# Gardener and tree

**Problem Statement:**
You have a tree with n nodes and a gardener who performs k operations. In each operation, the gardener removes all
leaf nodes (nodes with degree ≤ 1) simultaneously. After k operations, find how many nodes remain in the tree.
The solution involves simulating the process by repeatedly identifying and removing leaf nodes in each iteration.
Use BFS/level-order traversal to process nodes level by level, updating degrees as nodes are removed, and continue
until k operations are completed or no nodes remain.

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