# L - Deque

**Problem Statement:**
There are N integers in a deque (double-ended queue). Two players take turns removing either the leftmost or rightmost
element and adding its value to their score. The first player wants to maximize the score difference (their score minus
second player's score), while the second player wants to minimize it. Find the final score difference if both play optimally.
This is a classic interval DP problem where dp[l][r] represents the maximum advantage the current player can achieve on subarray [l,r].

Tags: game

```cpp
#include <bits/stdc++.h>

using namespace std;

long long dp[3001][3001];

int main() {

	int n;
	cin >> n;

	vector<int> a(n);
	for (int& x : a) cin >> x;

	for (int i = 0; i < n; ++i) dp[i][i] = a[i];

	for (int i = n - 1; i >= 0; i--)
		for (int j = i + 1; j < n; ++j)
			dp[i][j] = max(a[i] - dp[i + 1][j], a[j] - dp[i][j - 1]);
	cout << dp[0][n - 1] << '\n';
}
```