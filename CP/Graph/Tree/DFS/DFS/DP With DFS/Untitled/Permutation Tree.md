# Permutation Tree

**Problem Statement:**
Given a tree with n nodes, each node has a value from 1 to n forming a permutation. You need to count the number of
ways to assign values to nodes such that for every node, the values in its subtree form a contiguous range when sorted.
Use tree DP with DFS to solve this problem. For each subtree, calculate how many valid permutations can be assigned
considering the constraint that subtree values must be contiguous. The key insight is that if a subtree has k nodes,
its values must be some contiguous range of length k from the overall permutation.

[Problem - 1856E1 - Codeforces](https://codeforces.com/problemset/problem/1856/E1)

```cpp
#define int long long
 
class solve{
    public:
    solve(){
        int n;
        cin>>n;
        vector<vector<int>>graph(n);
        for(int i = 1; i < n; i++){
            int a;
            cin>>a;
            a--;
            graph[a].push_back(i);
            graph[i].push_back(a);
        }
        debug(graph);
        vector<int>subtreesize(n,0);
        int ans = 0;
        function<void(int,int)>dfs = [&](int src,int par){
            bool leaf = 1;
            vector<int>temp;
            int size = 0;
            for(auto node: graph[src]){
                if(node != par){
                    dfs(node,src);
                    leaf = 0;
                    size+=subtreesize[node];
                    temp.push_back(subtreesize[node]);
                }
            }
            debug(temp);
            subtreesize[src] = size + 1;
            if(leaf == 1){
                return;
            }
            vector<int>dp(size+1,0);
            int m = temp.size();
            dp[0] = 1;
            for(int i = 0; i < m; i++){
                for(int j = size - temp[i]; j >= 0; j--){
                    if(dp[j] != 0){
                        dp[j+temp[i]] = 1;
                    } 
                }
            }
            cerr << src << ' ' << endl;
            debug(dp);
            int res = 0;
            for(int i = 0; i <= size; i++){
                if(dp[i] == 1){
                    res = max((size - i)*i,res);
                }
            }
            ans += res;
            // cout << src << ' ' << res << endl;
        };
        dfs(0,-1);
        cout << ans << endl;
    }
};
 
int32_t main() {
    int t=1;
    // cin>>t;
    while(t--){
        solve obj;
    }
    return 0;
}
```