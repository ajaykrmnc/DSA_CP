# Subordinates

Given the structure of a company, your task is to calculate for each employee the number of their subordinates.

```cpp
#include<bits/stdc++.h>
using namespace std;

vector<vector<int>>adj;
vector<int>ans;
void dfs(int node,int par=-1){
    int tmp=0;
    for(auto to : adj[node]){
        if(to==par)continue;
        dfs(to,node);
        tmp+=(1+ans[to]);
    }
    ans[node]=tmp;
}
 
 
int32_t main() {
    fastio();
    int n;
    cin>>n;
    adj.resize(n);
    ans.resize(n,0);
    for(int i=1;i<n;i++){
        int a;
        cin>>a;
        a--;
        adj[a].pb(i);
        adj[i].pb(a);
    }
    debug(adj);
    debug(ans);
    dfs(0);
    for(auto x: ans){
        cout<<x<<' ';
    }
    cout<<nline;
 
 
    return 0;
```