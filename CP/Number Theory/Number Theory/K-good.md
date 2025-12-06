# K-good

problem link: https://codeforces.com/contest/1656/problem/D

```cpp
#include<bits/stdc++.h>
 
using namespace std;
 
#define endl '\n'
 
typedef long long ll;
 
int main() {
    ios::sync_with_stdio(false);
	int T;
	cin >> T;
	while(T--) {
		ll n;
		cin >> n;
		ll x = n;
		while(x % 2 == 0) x /= 2;
		if(x == 1) {
			cout << -1 << endl;
		}
		else if(x <= 2e9 && (x*(x+1))/2 <= n) {
			cout << x << endl;
		}
		else {
			cout << 2*(n/x) << endl;
		}
	}
}
```