# Friendly Spiders

[Problem - D - Codeforces](https://codeforces.com/contest/1775/problem/D)

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

const int mod= 1e9+7;
const int maxn=3e5+1;
const int inf=5e18;
const int minf=-inf;
vector<int>spf(maxn,0);

void seive(){
    spf[1]=1;
    for(int i=2;i<maxn;i++){
        if(!spf[i]){
            spf[i]=i;
            for(int j=i*i;j<maxn;j+=i){
                if(!spf[j]) spf[j]=i;
            }
        }
    }
}
bool solve(){
    int n,src,tgt;
    cin>>n;
    vector<int>v(n),dis(2*maxn,-1),par(2*maxn,-1);
    vector<vector<int>>adj(2*maxn);
    mac(i,0,n)cin>>v[i];
    cin>>src>>tgt;
    src--,tgt--;
    for(int i=0;i<n;i++){
        while(spf[v[i]]>1){
            adj[i].pb(maxn+spf[v[i]]);
            adj[maxn+spf[v[i]]].pb(i);
            v[i]/=spf[v[i]];
        }
    }
    queue<int>q;
    q.push(src);
    dis[src]=1;
    par[src]=-1;
    while(!q.empty()){
        int curr=q.front();
        q.pop();
        for(int child: adj[curr]){
            if(dis[child]==-1){
                par[child]=curr;
                dis[child]=dis[curr]+1;
                q.push(child);
            }
        }
    }
    if(dis[tgt]==-1){
        return false;
    }
    int node= tgt;
    vector<int>path;
    while(node!=-1){
        if(node<n){
            path.push_back(node);
        }
        node=par[node];
    }
    reverse(path.begin(),path.end());
    cout<<(dis[tgt]+1)/2<<endl;
    for(int node: path){
        cout<<node+1<<' ';
    }
    return true;
}

```