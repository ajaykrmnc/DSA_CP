# Score of a tree

**Problem Statement:**
Given a tree with n nodes, calculate the score of the tree. The score is typically defined as the sum of distances between
all pairs of nodes, or some other tree-based metric. This problem involves tree traversal, distance calculations, and
possibly dynamic programming on trees. Use DFS to calculate distances or apply tree DP techniques to compute the required
score efficiently. The exact scoring function depends on the specific problem requirements.

Select: unsolved

```cpp
void solve(){
    int n=1,m=0;
    string s;
    cin>>n;
    vvi adj(n);
    vi deg(n,0);
    for(int i=0;i<n-1;i++){
        int u=0,v=0;
        cin>>u>>v;
        u--,v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }
    if(n==1){
        cout<<"1\n";
        return;
    }
    vi levels(n,0);
    queue<int> q;
    deg[0]++;
    for(int i=0;i<n;i++){
        if(deg[i]==1){
           q.push(i);
           levels[i]=1;
        }
    }
    int lv=1;
    while(q.size()){
 
        lv++;
        int sz=q.size();
        while(sz--){
            int node=q.front();
            q.pop();
            for(auto& nb:adj[node]){
                deg[nb]--;
                if(deg[nb]==1){
                    levels[nb]=lv;
                    q.push(nb);
                }
            }
 
        }
    }
    int res=0;
    int mul=power(2,n-1);
    for(auto& i:levels){
        res+=mul*i;
        res%=MOD;
    }
    cout<<res<<"\n";
 
 
    
}
```