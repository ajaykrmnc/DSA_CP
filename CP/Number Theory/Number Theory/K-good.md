# K-good

**Problem Statement:**
A positive integer n is k-good if it can be expressed as a sum of k positive integers that give k distinct remainders when divided by k.
Given n, find some k ≥ 2 such that n is k-good, or determine if no such k exists. The problem involves number theory concepts
like modular arithmetic and constructive algorithms. Key insight: n is k-good if n ≥ k*(k+1)/2 and n has the right structure
based on its prime factorization. The solution typically involves checking if n can be written as sum of consecutive integers
starting from different remainders modulo k.

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