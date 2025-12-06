# Tree distance 1

```cpp
#include<bits/stdc++.h>
using namespace std;
 
//dist[0][i]= distance from node a to node i
// dist[1][i]= distance form node b to node i
// where a and b are end point of diameter
int dist[2][200001];
vector<int>adj[200001];
 
int dfs(int u,int p,int d,int i){
    dist[i][u]=d;
    int opt=-1;
    for(int v: adj[u]){
        if(v!=p){
            int x=dfs(v,u,d+1,i);
            if(opt==-1||dist[i][x]>dist[i][opt]) opt=x;
        }
    }
    return opt==-1 ? u : opt;
}
int main(){
    int n;
    cin>>n;
    for(int i=0;i<n-1;i++){
        int a,b;
        cin>>a>>b;
        --a;
        --b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    // first find node a by finding the farthest nodd
    int mxNode=dfs(0,0,0,0);
 
    // then find node b this step also computes the distance from a to every integer
 
    int mxNode2= dfs(mxNode,mxNode,0,0);
 
    dfs(mxNode2,mxNode2,0,1);
    for(int i=0;i<n;i++){
        cout<<max(dist[0][i],dist[1][i])<<'\n';
    }
    return 0;
}
```