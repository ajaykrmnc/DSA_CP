# Ksyusha and Chinchilla

**Problem Statement:**
Given a tree with n nodes, determine if it can be partitioned into subtrees where each subtree has exactly 3 nodes. If possible, output the edges to remove to create such a partition. Use DFS to calculate subtree sizes and identify edges that can be removed when a subtree has exactly 3 nodes. The key insight is that we can remove an edge if the subtree rooted at the child has exactly 3 nodes, and no node should have more than 2 children to ensure valid partitioning.

```cpp
#include <bits/stdc++.h>

vector<vector<int>>adj;
vector<pair<int,int>>ans;
vector<int>subTreeSize;
int flag=0;

void dfs(int src,int par=-1){
    int cnt=0;
    int noOfNodes=1;
    for(auto child: adj[src]){
        if(child==par)continue;
        cnt++;
        dfs(child,src);
        noOfNodes+=(subTreeSize[child]);
    }
    if(noOfNodes==3){
        ans.pb({src,par});
        adj[src].clear();
        noOfNodes=0;
    }
    subTreeSize[src]=noOfNodes;
    if(cnt>2)flag=1;
}
int32_t main()
{
    speed()
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        adj.resize(n);
        subTreeSize.resize(n);
        map<pair<int,int>,int>mp;
        for(int i=0;i<n-1;i++){
            int a,b;
            cin>>a>>b;
            a--;b--;
            mp[{a,b}]=i+1;
            mp[{b,a}]=i+1;
            adj[a].pb(b);
            adj[b].pb(a);
        }
        debug(adj);
        dfs(0);
        int cnt=0;
        if(ans.size()*3!=n){
            cout<<-1<<nline;
            adj.clear();
            ans.clear();
            continue;
        }
        cout<<ans.size()-1<<nline;
        for(auto [x,y]: ans){
            if(y!=-1){
                cout<<mp[{x,y}]<<" ";
            }
        }
        cout<<nline;
        debug(adj);
        debug(ans);
        adj.clear();
        ans.clear();
        
    }

    return 0;
}
```