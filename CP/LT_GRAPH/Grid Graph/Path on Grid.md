# Path on Grid

URL: https://cses.fi/problemset/task/1193

```cpp
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
    int st,en;
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        for(int j=0;j<m;j++){
            if(s[j]=='#'){
                tab[i][j]=1;
            }
            else tab[i][j]=0;
            if(s[j]=='A')st=i*m+j;
            else if(s[j]=='B'){en=i*m+j;}
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
    queue<int>q;
    q.push(st);
    vector<pair<int,char>>par(n*m,{-1,' '});
    vector<int>vis(n*m,0);
    vis[st]=1;
    while(!q.empty()){
        int x=q.front();
        q.pop();
        for(auto y: adj[x]){
            if(!vis[y.first]){
                vis[y.first]=true;
                par[y.first]={x,y.second};
                q.push(y.first);
            }
        }
    }
    if(!vis[en]){
        cout<<"NO"<<nline;
        return 0;
    } else {
        cout<<"YES"<<nline;
        string ans="";
        int prev=en;
        for(int v=par[en].first; v !=-1; v=par[v].first){
            ans+=(par[prev].second);
            prev=v;
        }
        cout<<ans.size()<<nline;;
        reverse(all(ans));
        cout<<ans<<nline;
    } 
 
    return 0;
}
```