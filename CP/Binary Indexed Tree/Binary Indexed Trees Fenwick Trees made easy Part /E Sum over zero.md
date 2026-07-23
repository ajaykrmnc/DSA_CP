# E. Sum over zero

**Problem Statement:**
Given an array, find the maximum length of a subarray with sum greater than zero. This problem uses prefix sums and
coordinate compression with Fenwick Tree for efficient range maximum queries. Convert the problem to finding the maximum
difference between indices with specific prefix sum constraints. Use coordinate compression to map prefix sums to a
smaller range, then apply dynamic programming with BIT to track maximum values efficiently. The solution runs in O(n log
n) time complexity.

```cpp
#include<bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;
using uint = unsigned int;
using ull = unsigned long long;
template<typename T>
using pair2 = pair<T, T>;
using pii = pair<int, int>;
using pli = pair<ll, int>;
using pll = pair<ll, ll>;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
ll myRand(ll B) {
	return (ull)rng() % B;
}

#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second

clock_t startTime;
double getCurrentTime() {
	return (double)(clock() - startTime) / CLOCKS_PER_SEC;
}

const int N = 200200;
int n, m;
int dp[N];
ll a[N];
ll xs[N];
int fenv[N];

void setPoint(int v, int x) {
	for (; v < N; v |= v + 1)
		fenv[v] = max(fenv[v], x);
}
int getMax(int r) {
	int res = 0;
	for (; r >= 0; r = (r & (r + 1)) - 1)
		res = max(res, fenv[r]);
	return res;
}

int main()
{
	startTime = clock();
	//	freopen("input.txt", "r", stdin);
	//	freopen("output.txt", "w", stdout);

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%lld", &a[i + 1]);
		a[i + 1] += a[i];
	}
	for (int i = 0; i <= n; i++)
		xs[i] = a[i];
	sort(xs, xs + n + 1);
	m = unique(xs, xs + n + 1) - xs;
	for (int i = 0; i <= n; i++) {
		a[i] = lower_bound(xs, xs + m, a[i]) - xs;
		a[i] = m - 1 - a[i];
	}
	for (int i = n; i >= 0; i--) {
		if (i < n) {
			dp[i] = max(dp[i + 1], getMax(a[i]) - i);
		}
		setPoint(a[i], dp[i] + i);
	}
	printf("%d\n", dp[0]);

	return 0;
}
```

[https://youtu.be/HkGdJod75Po?t=2852](https://youtu.be/HkGdJod75Po?t=2852)

[Fenwick Tree - Algorithms for Competitive Programming](https://cp-algorithms.com/data_structures/fenwick.html)

