# K- Stones

**Problem Statement:**
There are K stones and two players take turns removing stones. On each turn, a player can remove a[i] stones for any valid i (1 ≤ i ≤ N). The player who cannot make a move loses. Determine who wins if both players play optimally. This is a classic game theory DP problem where dp[i] represents whether the current player can win with i stones remaining. A position is winning if there exists at least one move that leads to a losing position for the opponent. Use the concept of winning and losing states in combinatorial game theory.

Tags: game

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, k;
	cin >> n >> k;
	vector<int> a(n);
	for (int& x : a) cin >> x;
	vector<bool> dp(k + 1);
	for (int i = 1; i <= k; ++i)
		for (int j : a)
			if (i >= j && !dp[i - j])
				dp[i] = 1;
	cout << (dp[k] ? "First" : "Second") << '\n';
}
```