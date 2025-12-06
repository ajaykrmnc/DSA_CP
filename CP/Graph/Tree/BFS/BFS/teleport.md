# teleport

problem link: bfs

```cpp

int32_t main() {
    fastio();
    int t=1;
    cin>>t;
    int tmp=0;
    while(t--){
        int n;
        tmp++;
        cin>>n;
        int from,to;
        cin>>from>>to;
        from--;to--;
        vector<vector<pair<int,int>>>adj(n);
        for(int i=0;i<n-1;i++){
            int a,b,w;
            cin>>a>>b>>w;
            a--;b--;
            adj[a].pb({b,w});
            adj[b].pb({a,w});
        }
        queue<int>q;
        q.push(from);
        vector<int>arr1(n,0),arr2(n,0),vis(n,0);
        vis[from]=1;
        while(q.size()){
            int node= q.front();
            q.pop();
            for(auto [child,w]: adj[node]){
                if(!vis[child] and child!=to){
                    int res = (w ^ arr1[node]);
                    arr1[child] = res;
                    vis[child]=1;
                    q.push(child);
                }
            }
            
        }
        debug(adj);
        for(auto &x: vis){
            x=0;
        }
        q.push(to);
        vis[to]=1;
        while(q.size()){
            int node= q.front();
            q.pop();
            for(auto [child,w]: adj[node]){
                if(!vis[child]){
                    int res= (w  ^ arr2[node]);
                    arr2[child] = res;
                    vis[child]=1;
                    q.push(child);
                }
            }
        }
        debug(arr1);
        debug(arr2);
        set<int>st;
        if(arr2[from]==0){
            cout<<"YES"<<nline;
            continue;
        }
        for(int i=0;i<n;i++){
            if( i!= to )
            st.insert(arr1[i]);
        }
        debug(st);
        int flag=0;
        for(int i= 0;i<n;i++){
            if( i== to)continue;
            debug(arr2[i]);
            if(st.find((arr2[i]))!=st.end()){
                flag=1;
            }
        }
        if(flag){
            cout<<"YES"<<nline;
        }else{
            cout<<"NO"<<nline;
        }

    
    }

    return 0;

}
```