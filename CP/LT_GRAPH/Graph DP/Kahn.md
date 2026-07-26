# Kahn

URL: https://cses.fi/problemset/task/1679

You have to complete n courses. There are m requirements of the form "course a has to be completed before course b". Your task is to find an order in which you can complete the courses.

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
    vector<int>indeg(n+1,0);
    for(int i=0;i<m;i++){
        int a,b;
        cin>>a>>b;
        indeg[b]++;
        adj[a].push_back(b);
    }
    queue<int>q;
    vector<int>vis(n+1,0);
    for(int i=1;i<=n;i++){
        if(indeg[i]==0){
            q.push(i);
            vis[i]=0;
        }
    }
    
    vector<int>ans;
    while(!q.empty()){
         int node=q.front();
         q.pop();
         ans.pb(node);
         for(auto x: adj[node]){
             if(vis[x]==0){
                indeg[x]--;
                if(indeg[x]==0){
                    q.push(x);
                    vis[x]=true;
                }
             }
         }
    }
    if(ans.size()!=n){
        cout<<"IMPOSSIBLE"<<nline;
        return 0;
    }
    for(auto x: ans){
        cout<<x<<' ';
    }
 
    return 0;
}
```