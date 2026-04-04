# Train spitting

**Problem Statement:**
You have a train system with n stations connected by railways. The train can split into multiple parts at certain stations.
Given the train's route and splitting rules, determine the final configuration or solve a related optimization problem.
This involves graph traversal, possibly with state tracking for different train parts, and may require dynamic programming
or greedy approaches depending on the specific constraints and objectives of the train splitting problem.

problem link: https://codeforces.com/problemset/problem/1776/F

```cpp
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;

#define osl tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update>
#define ll long long
#define ld long double
#define forl(i, a, b) for(ll i = a; i < b; i++)
#define rofl(i, a, b) for(ll i = a; i > b; i--)
#define fors(i, a, b, c) for(ll i = a; i < b; i += c)
#define fora(x, v) for(auto x : v)
#define vl vector<ll>
#define vb vector<bool>
#define pub push_back
#define pob pop_back
#define fbo find_by_order
#define ook order_of_key
#define yesno(x) cout << ((x) ? "YES" : "NO")
#define all(v) v.begin(), v.end()

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