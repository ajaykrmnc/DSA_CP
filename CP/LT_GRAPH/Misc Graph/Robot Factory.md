# Robot Factory

**Problem Statement:**
You have an n×m grid representing a robot factory. Some cells have walls that block movement in certain directions.
Find the number of connected components where robots can move freely. Two cells are connected if robots can move between
them without crossing walls. Use DFS or BFS to explore each connected component, considering the wall constraints that
prevent movement in blocked directions. This is a graph connectivity problem with directional constraints.

problem link: https://codeforces.com/contest/1600/problem/J

```cpp
vector<vector<int> >v(1010,vector<int>(1010)),vis;
int cnt=0;
vector<pair<int,int> >dir{{-1,0},{0,1},{1,0},{0,-1}};
 
int isin(int x,int y){
    if(x>-1 and x<n and y>-1 and y<m)
        return 1;
    return 0;
}
 
void dfs(int x,int y)
{
    vis[x][y]=1;
    int num=v[x][y];
    ++cnt;
    for(int i=0;i<4;i++){
        if(str[num][i]=='1')
            continue;
        if(isin(x+dir[i].first,y+dir[i].second) and !vis[x+dir[i].first][y+dir[i].second])
            dfs(x+dir[i].first,y+dir[i].second);
    }
}
 
 
int main()
{
    for(int i=0;i<16;i++)
        str[i]=dtob(i);
    cin >> n >> m;
    vis=v;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin >> v[i][j];
            vis[i][j]=0;
        }
    }
    vector<int>ans;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(!vis[i][j])
            {
                cnt=0;
                dfs(i,j);
                ans.push_back(cnt);
            }
        }
    }
    sort(ans.begin(),ans.end(),greater<int>());
    VecPrint<int>(ans);
}
```