# Tree Matching

**Problem Statement:**
You are given a tree consisting of n nodes. A matching is a set of edges where each node is an endpoint of at most one
edge. Your task is to find the maximum number of edges in a matching. This is a classic tree DP problem where for each
node we decide whether to include it in the matching or not. We maintain two states: dp[node][0] = maximum matching in
subtree of node where node is not matched, and dp[node][1] = maximum matching where node is matched with its parent. The
answer is `dp[root][0]`. Time complexity is O(n) with a single DFS traversal.

[DP on Trees - Introduction](https://usaco.guide/gold/dp-trees?lang=cpp#taking-no-edges)

```cpp

vector<vector<int>>adj;
int dp[200005][2];
void solve(int node,int par=-1){
  dp[node][0]=0,dp[node][1]=0;
  int leaf=1;
  for(auto to: adj[node]){
    if(to!=par){
      leaf=0;
      solve(to,node);
    }
  }
  if(leaf)return;
  // build pre and suf for the array vector<int>suf,pre;
  for(auto to: adj[node]){
    if(to==par)continue;
    pre.pb(max(dp[to][0],dp[to][1]));
    suf.pb(max(dp[to][0],dp[to][1]));
  }
  for(int i=1;i<pre.size();i++){
    pre[i]+=pre[i-1];
  }
  for(int i=suf.size()-2;i>=0;i--){
    suf[i]+=suf[i+1];
  }
  debug(suf);
  debug(pre);
  dp[node][0]=suf[0];
  int c_no=0;
  for(auto to: adj[node]){
    if(to==par)continue;
    int leftChild=(c_no==0) ? 0: pre[c_no-1];
    int rightChild=(c_no==int(suf.size())-1) ? 0: suf[c_no+1];
    dp[node][1]=max(dp[node][1],1+leftChild+rightChild+dp[to][0]);
    c_no++;
  }

}

int32_t main() {
  fastio();
  int n;
  cin>>n;
  adj.resize(n);
  for(int i=0;i<n-1;i++){
    int a,b;
    cin>>a>>b;
    a--;b--;
    adj[a].pb(b);
    adj[b].pb(a);
  }
  debug(adj);
  // dfs(0);
  solve(0);
  cout<<max(dp[0][1],dp[0][0])<<nline;

  return 0;
```

---

