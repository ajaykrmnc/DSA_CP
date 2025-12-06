# 2 Groups

URL: https://cses.fi/problemset/task/1668/

There are n pupils in Uolevi's class, and m friendships between them. Your task is to divide the pupils into two teams in such a way that no two pupils in a team are friends. You can freely choose the sizes of the teams.

```cpp
#include <bits/stdc++.h>
using namespace std;
#define pb push_back 
#define int long long
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define nline '\n'
#define mac(i,x,y) for(int i=(int)x; i<y; i++)
#define speed() ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
 
int32_t main()
{
    speed()
    int n,m;
    cin>>n>>m;
    vector<vector<int>>adj(n+1);
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    int flag=0;
    vector<pair<int,bool>>vis(n+1,{0,0});
    for(int i=1;i<=n;i++){
        queue<int>q;
        q.push(i);
        if(!vis[i].second){
            vis[i]={1,0};
        }
        while(!q.empty()){
            int node=q.front();
            q.pop();
            for(auto x: adj[node]){
                if(!vis[x].first){
                    vis[x].first=true;
                    q.push(x);
                    vis[x].second=(1^vis[node].second);
                }else {
                    if(vis[x].second==vis[node].second)
                        flag=1;
                }
            }
        }
    }
    if(flag){
        cout<<"IMPOSSIBLE"<<nline;
        return 0;
    }else{
        for(int i=1;i<=n;i++){
                cout<<vis[i].second+1<<' ';
        }
    }
 

 
 
    return 0;
}
```