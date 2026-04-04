# Train spliitting

**Problem Statement:**
Given a graph with n nodes and m edges, assign each edge a color from 1 to k such that for any two nodes, all paths between them use the same set of colors. Find the minimum k and output the coloring. The solution involves analyzing the graph structure - if the graph is not complete, we can use 2 colors by finding a node with degree < n-1. Otherwise, we need 3 colors and can use a specific coloring strategy based on a spanning tree.

problem link: https://codeforces.com/contest/1776/problem/F

```cpp

const ll N = 2e5 + 4;
const ll mod = 1e9 + 7;
// const ll mod = 998244353;

void panipuri() {
	ll n, m = 0, k = 2, c = 0, sum = 0, q = 2, ans = 0, p = 1;
	string s;
	bool ch = true;
	cin >> n>>m;
	vl a(m);
	vl v[n+1];
	map<pair<ll,ll>,ll> mp;
	forl(i, 0, m) {
		ll x,y;
		cin>>x>>y;
		v[x].pub(y);
		v[y].pub(x);
		mp[{x,y}]=i;
		mp[{y,x}]=i;
	}
	forl(i,1,n+1){
		if(v[i].size()<n-1){
			cout<<"2\n";
			forl(i,0,m) a[i]=2;
			fora(x,v[i]) a[mp[{x,i}]]=1;
			fora(x,a) cout<<x<<' ';
			return;
		}
	}
	forl(i,0,m) a[i]=3;
	cout<<"3\n";
	a[mp[{1,2}]]=1;
	forl(i,3,n+1) a[mp[{1,i}]]=2;
	fora(x,a) cout<<x<<' ';
	return;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
	int laddu = 1;
	cin >> laddu;
	forl(i, 1, laddu + 1) {
		// cout << "Case #" << i << ": ";
		panipuri();
		cout << '\n';
	}
}
```