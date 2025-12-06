# Social Network

problem link: https://codeforces.com/problemset/problem/1609/D

```cpp

#define speed() ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
struct DSU {
  vector<int> par, rnk, sz;
  int c;
  DSU(int n) : par(n + 1), rnk(n + 1, 0), sz(n + 1, 1), c(n) {
    for (int i = 1; i <= n; ++i) par[i] = i;
  }
  int find(int i) {
    return (par[i] == i ? i : (par[i] = find(par[i])));
  }
  bool same(int i, int j) {
    return find(i) == find(j);
  }
  int get_size(int i) {
    return sz[find(i)];
  }
  int count() {
    return c;    //connected components
  }
  int merge(int i, int j) {
    if ((i = find(i)) == (j = find(j))) return -1;
    else --c;
    if (rnk[i] > rnk[j]) swap(i, j);
    par[i] = j;
    sz[j] += sz[i];
    if (rnk[i] == rnk[j]) rnk[j]++;
    return j;
  }
};
 
 
 
int main()
{
    
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int n,d,u,v;
	cin>>n>>d;
 
	DSU ds(n);
 
	int x=0;
 
	for(int i=0; i<d; i++){
		cin>>u>>v;
		if(ds.same(u,v)){
			x++;
		}
		else{
			ds.merge(u,v);
		}
 
		vector<bool> vis(n+1,false);
		vector<int> v;
 
 
		mac(i,1,n+1){
			if(!vis[ds.find(i)]){
				v.pb(ds.get_size(i));
				vis[ds.find(i)]=true;
			}
		}
 
		sort(all(v));
		int m = v.size();
 
		vector <bool> vis2(m,false);
 
		int ans=0;
		int cnt=1+x;
 
 
		for(int i=m-1; i>=0 and cnt>0; i--){
			cnt--;
			ans += v[i];
		}
		cout<<ans-1<<'\n';
 
	}

	
	return 0;
}
```