# Tree Tag

**Problem Statement:**
Alice and Bob play a game on a tree. Alice starts at node a and Bob starts at node b. They take turns moving to adjacent
nodes, with Alice going first. Alice wins if she can reach Bob's current position, while Bob wins if he can avoid Alice
for a certain number of moves. The game involves strategic movement on the tree where Alice tries to catch Bob and Bob
tries to stay away. The solution involves analyzing tree distances, optimal strategies, and understanding when Alice can
guarantee a win based on the tree structure and starting positions.

problem link: https://codeforces.com/contest/1404/problem/B

```cpp
struct LCA {
  vector<int> height, euler, first, segtree;
  vector<bool> visited;
  int n;

  LCA(vector<vector<int>> &adj, int root = 0) {
    n = adj.size();
    height.resize(n);
    first.resize(n);
    euler.reserve(n * 2);
    visited.assign(n, false);
    dfs(adj, root);
    int m = euler.size();
    segtree.resize(m * 4);
    build(1, 0, m - 1);
  }

  void dfs(vector<vector<int>> &adj, int node, int h = 0) {
    visited[node] = true;
    height[node] = h;
    first[node] = euler.size();
    euler.push_back(node);
    for (auto to : adj[node]) {
      if (!visited[to]) {
        dfs(adj, to, h + 1);
        euler.push_back(node);
      }
    }
  }

  void build(int node, int b, int e) {
    if (b == e) {
      segtree[node] = euler[b];
    } else {
      int mid = (b + e) / 2;
      build(node << 1, b, mid);
      build(node << 1 | 1, mid + 1, e);
      int l = segtree[node << 1], r = segtree[node << 1 | 1];
      segtree[node] = (height[l] < height[r]) ? l : r;
    }
  }

  int query(int node, int b, int e, int L, int R) {
    if (b > R || e < L)
      return -1;
    if (b >= L && e <= R)
      return segtree[node];
    int mid = (b + e) >> 1;

    int left = query(node << 1, b, mid, L, R);
    int right = query(node << 1 | 1, mid + 1, e, L, R);
    if (left == -1) return right;
    if (right == -1) return left;
    return height[left] < height[right] ? left : right;
  }

  int lca(int u, int v) {
    int left = first[u], right = first[v];
    if (left > right)
      swap(left, right);
    return query(1, 0, euler.size() - 1, left, right);
  }
};
int32_t main()
{
  speed()
  int t;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    int a,b,da,db;
    cin>>a>>b>>da>>db;
    a--;b--;
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
    int dist_ab=tree.height[a]+tree.height[b]-2*tree.height[tree.lca(a,b)];
    // case 1
    debug(dist_ab);
    debug(diam);
    if(dist_ab<=da){
      cout<<"Alice";
    }else if(2*da>=diam){
      cout<<"Alice";
    }else if(db>2*da){
      cout<<"Bob";
    }else{
      cout<<"Alice";
    }
    cout<<nline;
  }

  return 0;
}
```
