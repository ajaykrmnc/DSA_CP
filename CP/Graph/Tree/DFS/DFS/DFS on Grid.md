# DFS on Grid

URL: https://cses.fi/problemset/task/1194

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
 
int n,m,st;
 
bool isValid(int i, int j,int n,int m){
    if(i>=n||i<0||j>=m||j<0)
    return false;
    return true;
}
 
queue<int>q;
void bfs(vector<vector<pair<int,char>>>&adj,vector<int>&vis){
    q.push(st);
    vis[st]=true;
    vector<pair<pair<int,char>,char>>par(n*m,{{NULL,NULL},'M'});
    par[st]={{-1,'\0'},'A'};
    while(!q.empty()){
        int x=q.front();
        q.pop();
        for(auto y: adj[x]){
            if(!vis[y.first]){
                q.push(y.first);
                vis[y.first]=true;
                par[y.first]={{x,y.second},par[x].second};
            }
        }
    }
    string ans;
    int flag=0;
    for(int i=0;i<n*m;i++){
        if(i/m==0||i/m==n-1||i%m==0||i%m==m-1){
            if(par[i].second=='A'){
                flag=1;
                for(int v=i;par[v].first.first!=-1;v=par[v].first.first){
                    ans+=par[v].first.second;
                }
                break;
            }
        }
    }
    if(flag){
        cout<<"YES"<<nline;
        reverse(all(ans));
        cout<<ans.size()<<nline;
        cout<<ans<<nline;
    }else {
        cout<<"NO"<<nline;
    }
}
 
int32_t main()
{
    speed()
    cin>>n>>m;
    int tab[n][m];
    vector<int>vis(n*m,0);
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        for(int j=0;j<m;j++){
            if(s[j]=='#'){
                tab[i][j]=1;
            }
            else tab[i][j]=0;
            if(s[j]=='A')st=i*m+j;
            else if(s[j]=='M'){q.push(i*m+j);vis[i*m+j]=true;}
        }
    }
    pair<int,int>aspas[4]= {{0,1},{-1,0},{1,0},{0,-1}};
    char dir[4]={'R','U','D','L'};
    vector<vector<pair<int,char>>>adj(n*m);
 
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(tab[i][j]==0)
            for(int k=0;k<4;k++){
                auto x=aspas[k];
                if(isValid(i+x.first,j+x.second,n,m)&&tab[i+x.first][j+x.second]==0){
                    adj[i*m+j].pb({(i+x.first)*m+j+x.second,dir[k]});
                }
            }
        }
    }
    bfs(adj,vis);
 
    return 0;
}
```