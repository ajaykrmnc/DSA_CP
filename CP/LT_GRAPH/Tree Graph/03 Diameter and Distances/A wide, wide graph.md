# A wide, wide graph

**Problem Statement:**
Given a tree with n nodes, for each k from 1 to n, find the minimum number of nodes that need to be removed such that
the remaining tree has diameter at most k. The diameter of a tree is the longest path between any two nodes. Use tree
diameter algorithms to find the endpoints of the diameter, then for each node calculate its maximum distance to either
endpoint. Sort these distances and use binary search to find how many nodes to remove for each k. This problem combines
tree diameter computation with optimization techniques.

[Problem - 1805D - Codeforces](https://codeforces.com/problemset/problem/1805/D)

```cpp

int32_t main()
{
  speed()
  int n;
  cin>>n;
  vector<vector<int>>adj(n);
  for(int i=0;i<n-1;i++){
    int a,b;
    cin>>a>>b;
    a--;b--;
    adj[a].pb(b);
    adj[b].pb(a);
  }
  LCA tree(adj);
  int node=0;
  int mx=0;
  for(int i=0;i<n;i++){
    int dist=tree.height[i];
    if(dist>mx){
      node=i;
      mx=dist;
    }
  }
  int diam=0;
  int en=0;
  for(int i=0;i<n;i++){
    int lca=tree.lca(i,node);
    int dist=tree.height[node]+tree.height[i]-2*tree.height[lca];
    if(dist>diam){
      en=i;
      diam=dist;
    }
  }
  vector<int>v(n);
  for(int i=0;i<n;i++){
    int lca1=tree.lca(i,node);
    int lca2=tree.lca(i,en);
    int dist1=tree.height[node]+tree.height[i]-2*tree.height[lca1];
    int dist2=tree.height[en]+tree.height[i]-2*tree.height[lca2];
    v[i]=max(dist1,dist2);
  }    sort(all(v));
  debug(node);
  debug(en);
  debug(v);
  for(int i=1;i<=n;i++){
    auto it=lower_bound(all(v),i);
    if(it==v.end()){
      cout<<n<<' ';
    }else{
      cout<<1+it-v.begin()<<' ';
    }
  }

  return 0;
}
```

