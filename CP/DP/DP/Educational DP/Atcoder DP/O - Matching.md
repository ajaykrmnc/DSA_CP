# O - Matching

**Problem Statement:**
There are N men and N women. For each man i and woman j, you know whether they are compatible (a[i][j] = 1) or not (a[i][j] = 0).
Find the number of ways to pair up all men and women such that each person is paired with exactly one person of the opposite
gender, and all pairs are compatible. This is a classic bitmask DP problem where dp[mask] represents the number of ways to
match the first popcount(mask) men with the women represented by the bitmask.

Tags: bitmask-dp

```cpp
#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;
const int MAX_N = 21;

bool compat[MAX_N][MAX_N];
int dp[1 << MAX_N];

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> compat[i][j];
		}
	}

	dp[0] = 1;

	for (int s = 0; s < (1 << N); s++) {
		int pair_num = __builtin_popcount(s);
		for (int w = 0; w < N; w++) {
			/*
			 * check that
			 * 1. this woman hasn't been paired already
			 * 2. she's also compatible with the {pair_num + 1}th man
			 */
			if ((s & (1 << w)) || !compat[pair_num][w])
				continue;

			// add the amount to future dp states
			dp[s | (1 << w)] += dp[s];
			dp[s | (1 << w)] %= MOD;
		}
	}

   	cout << dp[(1 << N) - 1] << endl;
}
```