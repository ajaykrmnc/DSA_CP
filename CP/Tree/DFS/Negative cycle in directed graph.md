# Negative cycle in directed graph

URL: https://cses.fi/problemset/task/1197

You are given a directed graph, and your task is to find out if it contains a negative cycle, and also give an example of such a cycle.

```cpp
class solve{
public:
	solve(){
     int n, m,q;
     cin>>n>>m;
      vector<vector<int>> g;
     
     for(int i=0;i<m;i++)
    {   vector<int>v(3);
        cin>>v[0]>>v[1]>>v[2];
        g.push_back(v);
    }
 
    vector<int>dist(n+1,inf);
    vector<int>parent(n+1,-1);
     dist[1]=0;
     int x;
  for(int i=0;i<n;i++){
     x=-1;
       for(auto it: g){
             int a=it[0];
             int b=it[1];
             int c=it[2];
             if(dist[a]+c<dist[b]){
                    dist[b]=dist[a]+c;
                    parent[b]=a;
                    x=b;
             }
       }
  }
 
   if(x==-1){
     cout<<"NO";
     return 0;
   }
 
   for(int i=0;i<n;i++){
        x=parent[x];
   }
    vector<int> cycle;
        for (int v = x;; v = parent[v]) {
            cycle.push_back(v);
            if (v == x && cycle.size() > 1)
                break;
        }
        reverse(cycle.begin(), cycle.end());
        cout<<"YES\n";
        for (int v : cycle)
            cout << v << ' ';
	 }
}
```