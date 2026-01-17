# Multisource BFS

**Problem Statement:**
Multisource BFS is a variation of BFS where we start the traversal from multiple source nodes simultaneously. Instead of starting
from a single source, we add all source nodes to the queue initially and then perform standard BFS. This technique is useful
for problems like finding the shortest distance from any source to all other nodes, or problems involving multiple starting points.
Common applications include finding the nearest exit in a maze with multiple exits, or calculating minimum time for all cells
to be affected when multiple sources spread simultaneously. Time complexity remains O(V + E) where V is vertices and E is edges.

```cpp
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
const int MAX_SIZE = 1 << 20;
vector<int> e[MAX_SIZE];
int step[MAX_SIZE];
bool visited[MAX_SIZE];
void solve() {
    int N, M;
    cin >> N >> M;
    for(int i = 1; i <= N; i++) {
        int A;
        cin >> A;
        while(A--) {
            int S;
            cin >> S;
            e[i].push_back(N + S);
            e[N + S].push_back(i);
        }
    }
    queue<int> qq;
    qq.push(N + 1);
    visited[N + 1] = 1;
    while(!qq.empty()) {
        int x = qq.front();
        qq.pop();
        for(int y: e[x]) {
            if(!visited[y]) {
                visited[y] = 1;
                qq.push(y);
                step[y] = step[x] + 1;
            }
        }
    }
    if(!visited[N + M]) {
        cout << "-1\n";
    } else {
        cout << step[N + M] / 2 - 1 << '\n';
    }
}
int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    solve();
}
```

[Editorial - TOYOTA MOTOR CORPORATION Programming Contest 2023#2 (AtCoder Beginner Contest 302)](https://atcoder.jp/contests/abc302/tasks/abc302_f/editorial?editorialLang=ja)

kindly upsolve this [problem](https://codeforces.com/contest/1775/problem/D)  on seive with graphs

This is a standard question on graph theory with sieve to make the adjancency list of O(nlogn) instead of O(n^2). By making edge between the prime factor of the number to that numbers. But how we can identify them that which node is virtual node and which node is real node then it can be found by adding the buffer variable like 3e5+10;

Implementations. And then the distance between the given two nodes can be found using the standard algorithm bfs. and with maintaining the parent of that vertices

```cpp
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
            v[i]/ =spf[v[i]];
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