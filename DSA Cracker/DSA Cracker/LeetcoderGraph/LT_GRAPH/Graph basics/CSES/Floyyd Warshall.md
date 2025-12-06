# Floyyd Warshall

URL: https://cses.fi/problemset/task/1672
Tags: floyyd warshall

There are n cities and m roads between them. Your task is to process q queries where you have to determine the length of the shortest route between two given cities.****

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
const int inf=LLONG_MAX;
int32_t main()
{
    speed()
    int n,m,q;
    cin>>n>>m>>q;
    vector<vector<pair<int,int>>>adj(n+1);
    int dp[n+1][n+1];
    for(int i=0;i<n+1;i++){
        for(int j=0;j<n+1;j++){
            if(i==j){
                dp[i][j]=0;
            }else 
            dp[i][j]=inf;
        }
    }
    for(int i=0;i<m;i++){
        int a,b,w;
        cin>>a>>b>>w;
        adj[a].pb({b,w});
        adj[b].pb({a,w});
        dp[a][b]=min(dp[a][b],w);
        dp[b][a]=min(dp[b][a],w);
    }
    
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            for(int k=1;k<=n;k++){
                if(dp[j][i]!=inf and dp[i][k]!=inf)
                dp[j][k]=min(dp[j][k],dp[j][i]+dp[i][k]);
            }
        }
    }
    for(int i=0;i<q;i++){
        int a,b;
        cin>>a>>b;
        if(dp[a][b]==inf){
            cout<<-1<<nline;
        }else 
        cout<<dp[a][b]<<nline;
    }
    return 0;
}
```