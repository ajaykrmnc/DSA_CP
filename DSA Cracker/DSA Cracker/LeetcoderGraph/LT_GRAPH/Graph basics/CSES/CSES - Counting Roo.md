# CSES - Counting Roo

**Problem Statement:**
Given an n×m grid with walls ('#') and empty cells ('.'), count the number of connected components of empty cells. Two empty cells are connected if you can move from one to another using only up, down, left, right moves through empty cells. This is a classic graph connectivity problem that can be solved using DFS or BFS. Convert the 2D grid to a graph representation and count connected components by traversing unvisited empty cells and marking all reachable cells in each component.

URL: https://cses.fi/problemset/task/1192

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
 
void dfs(vector<int>&vis,vector<vector<int>>&adj,int node){
    vis[node]=true;
    for(auto x: adj[node]){
        if(!vis[x]){
            dfs(vis,adj,x);
        }
    }
}
bool isValid(int i, int j,int n,int m){
    if(i>=n||i<0||j>=m||j<0)
    return false;
    return true;
}
 
int32_t main()
{
    speed()
    int n;
    cin>>n;
    int m;
    cin>>m;
    int tab[n][m];
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        for(int j=0;j<m;j++){
            if(s[j]=='#'){
                tab[i][j]=1;
            }else tab[i][j]=0;
        }
    }
    pair<int,int>aspas[4]= {{0,1},{-1,0},{1,0},{0,-1}};
    vector<vector<int>>adj(n*m);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(tab[i][j]==0)
            for(auto x: aspas){
                if(isValid(i+x.first,j+x.second,n,m)&&tab[i+x.first][j+x.second]==0){
                    adj[i*m+j].pb((i+x.first)*m+j+x.second);
                }
            }
        }
    }
    vector<int>vis(n*m,0);
    int cnt = 0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(!vis[i*m+j]&&tab[i][j]==0){
                dfs(vis,adj,i*m+j);
                cnt++;
            }
        }
    }
    cout<<cnt<<nline;
 
    return 0;
}
```