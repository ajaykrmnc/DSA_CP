# Tree xor

**Problem Statement:**
Given a tree with n nodes, each node has a value. You can perform operations to flip the values of all nodes in a subtree
(XOR with 1). Find the minimum number of operations needed to make all node values equal to 0. Use tree DP with DFS to
solve this problem. For each node, calculate the minimum operations needed for its subtree. The key insight is that if
a node's value is 1, you must perform an operation on its subtree. Use post-order traversal to ensure children are
processed before parents, allowing optimal decision making for each subtree.

[Problem - D - Codeforces](https://codeforces.com/contest/1882/problem/D)

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mylib/mydebug.h"
#else
#define debug(x)
#endif
#define ll long long
#define int long long 

class solve{
    public:
    solve(){
        int n;
        cin >> n;
        vector<int>v(n);
        for(auto &x: v){
            cin >> x;
        }
        vector<vector<int>>adj(n);
        for(int i = 0; i < n - 1; i++){
            int a, b;cin >> a >> b;a--;b--;
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        vector<vector<ll>>dp(n,vector<ll>(2,0));
        vector<int>subtreesize(n,0);
        function<void(int,int,int)>dfs = [&](int src,int par,int i){
            int num = (1 << i);
            int zero = 0, one = 0;
            subtreesize[src] = 1;
            for(auto node: adj[src]){
                if(node == par)continue;
                dfs(node,src,i);
                zero += dp[node][0];
                one += dp[node][1];
                subtreesize[src] += subtreesize[node];
            }
            int finalzero = 0, finalone = 0;
            if((num & v[src])){
                finalzero = one + num * subtreesize[src];
                finalone = one;
            }else{
                finalone = zero + num * subtreesize[src];
                finalzero = zero;
            }
            dp[src][0] = finalzero;
            dp[src][1] = finalone;
        };
        vector<ll>ans(n + 1,0);
        function<void(int,int,int)>dfs2 = [&](int src,int par,int i){
            for(auto node: adj[src]){
                if(node == par)continue;
                int num = (1 << i);
                // remove the contribution of child fro the src
                int needzero = dp[src][0],needone = dp[src][1];
                if((num & v[src])){
                    needzero -= (dp[node][1] + subtreesize[node] * num);
                    needone -= dp[node][1];
                }else{
                    needzero -= dp[node][0];
                    needone -= (dp[node][0] + subtreesize[node] * num);
                }

                // change the subtree size of the array
                subtreesize[src] -=  subtreesize[node];
                subtreesize[node] += subtreesize[src];

                // contribution of parent for the array
                // delete the contribution of src in the parent in the array

                if((num & v[node])){
                    dp[node][0] += (needone + subtreesize[src] * num);
                    dp[node][1] += needone;
                }else{
                    dp[node][0] += needzero;
                    dp[node][1] += (needzero + subtreesize[src] * num);
                }

                ans[node] += min(dp[node][0], dp[node][1]);

                dfs2(node, src, i);

                // remove the contribution of src from the node
                
                if((num & v[node])){
                    dp[node][0] -= (dp[src][1] + subtreesize[src] * num);
                    dp[node][1] -= dp[src][1];
                }else{
                    dp[node][0] -= dp[src][0];
                    dp[node][1] -= (dp[src][0] + subtreesize[src] * num);
                }
                // change the subtree size of the array
                subtreesize[node] -= subtreesize[src];
                subtreesize[src] +=  subtreesize[node];  
            }
        };
        int sum = 0;
        for(int i = 0; i < 20; ++i){
            for(int j = 0; j < n; ++j){
                dp[j][0] = 0;
                dp[j][1] = 0;
            }
            dfs(0,-1,i);
            dfs2(0,-1,i);
            sum += min(dp[0][1],dp[0][0]);
        }
        ans[0] = sum;
        for(int i = 0; i < n; ++i){
            cout << ans[i] << ' ';
        }
        cout << endl;
    }
};

int32_t main() {
    int t=1;
    cin>>t;
    while(t--){
        solve obj;
    }
    return 0;
}
```