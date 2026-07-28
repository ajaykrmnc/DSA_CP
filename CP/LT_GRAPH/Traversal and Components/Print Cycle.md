# Print Cycle

**Problem Statement:**
Given an undirected graph, find and print any cycle in the graph. If no cycle exists, print "IMPOSSIBLE". A cycle is a
path that starts and ends at the same vertex with at least 3 edges. This problem uses DFS to detect cycles by
maintaining parent information during traversal. When visiting a node, if we encounter an already visited node that is
not the parent, we've found a cycle. The solution involves tracking the path during DFS and reconstructing the cycle
when found. Time complexity is O(V + E) where V is vertices and E is edges.

URL: [Link](https://cses.fi/problemset/task/1669)

```cpp
#include <bits/stdc++.h>
using namespace std;
#define pb push_back #define int long long
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define nline '\n'
#define mac(i,x,y) for(int i=(int)x; i<y; i++)
#define speed() ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
int sv=-1,ev=-1;
int n,m;
vector<int>par;
vector<int>vis;
vector<vector<int>>adj;
bool dfs(int node,int bap=-1){
  vis[node]=true;
  par[node]=bap;
  for(auto x: adj[node]){
    if(x==bap)continue;
    if(vis[x]){
      sv=x;
      ev=node;
      return true;
    }
    if(!vis[x]){ if(dfs(x,node))
      return true;
    }
  }
  return false;
}

int32_t main()
{
  speed();
  cin>>n>>m;
  vis.resize(n+1,0);
  par.resize(n+1,-1);
  adj.resize(n+1);
  for(int i=0;i<m;i++){
    int a,b;
    cin>>a>>b;
    adj[a].pb(b);
    adj[b].pb(a);
  }
  for(int i=1;i<=n;i++){
    if(!vis[i]){
      if(dfs(i))
        break;
    }
  }
  if(sv==ev){
    cout<<"IMPOSSIBLE"<<nline;
    return 0;
  }
  int tv = ev;
	vector<int> ans;
	ans.push_back(ev);
	while(tv != sv)
	{
		ans.push_back(par[tv]);
		tv = par[tv];
	}
	ans.push_back(ev);
	cout << ans.size() << endl;
	for(auto c: ans)
	{
		cout << c << " ";
	}
  return 0;
}
```
