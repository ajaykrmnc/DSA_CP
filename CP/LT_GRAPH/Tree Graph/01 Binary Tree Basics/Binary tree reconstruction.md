# Binary tree reconstruction

**Problem Statement:**
Given three integers n0, n1, and n2, construct a binary string such that it has exactly n0 pairs of adjacent '00',
n1 pairs of adjacent '01' or '10', and n2 pairs of adjacent '11'. The goal is to find any valid binary string that
satisfies these constraints. The solution involves constructing an alternating pattern for the '01'/'10' pairs and
then inserting additional '0's and '1's to achieve the required counts of '00' and '11' pairs respectively.

problem link: https://codeforces.com/problemset/problem/1352/F

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n0, n1, n2;
		cin >> n0 >> n1 >> n2;
		if (n1 == 0) {
			if (n0 != 0) {
				cout << string(n0 + 1, '0') << endl;
			} else {
				cout << string(n2 + 1, '1') << endl;
			}
			continue;
		}
		string ans;
		for (int i = 0; i < n1 + 1; ++i) {
			if (i & 1) ans += "0";
			else ans += "1";
		}
		ans.insert(1, string(n0, '0'));
		ans.insert(0, string(n2, '1'));
		cout << ans << endl;
	}
}
```