# The Third letter

[Problem - H - Codeforces](https://codeforces.com/contest/1850/problem/H)

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mylib/mydebug.h"
#else
#define debug(x)
#endif
#define int long long
 
class solve{
    public:
    solve(){
        int n, m;
        cin >> n >> m;
        vector<vector<pair<int,int>>>adj(n);
        for(int i = 0; i < m; i++){
            int a, b, d;
            cin>>a >> b >>d;
            a--;b--;
            adj[a].push_back({b,d});
            adj[b].push_back({a,-d});
        }
        int flag = 0;
        vector<int>pos(n,0),vis(n,0);
        function<void(int,int)> dfs = [&](int src, int par){
            vis[src] = 1;
            for(auto [child,dist]: adj[src]){
                if(child != par){
                    if(!vis[child]){
                        pos[child] = pos[src] + dist;
                        dfs(child, src);
                    }else if(pos[child] != pos[src] + dist){
                        flag = 1;
                        return;
                    }
                }
            }
        };
        for(int i = 0; i < n; i++ ){
            if(!vis[i] and !flag){
                dfs(i,-1);
            }
        }
        if(flag){
            cout << "NO" << endl;
        }else{
            cout << "YES" << endl;
        }
    }
};
 
int32_t main() {
    int t=1;
    cin>>t;
    while(t--){
        solve obj;
    }
    return 0;
}
```