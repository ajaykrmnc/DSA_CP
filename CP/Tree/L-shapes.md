# L-shapes

**Problem Statement:**
Given an n×m grid with '_' and '.' characters, determine if all '_' characters form valid L-shapes. An L-shape consists
of exactly 3 '_' characters arranged in an L pattern (corner + two adjacent cells in perpendicular directions). Each '_'
must be part of exactly one L-shape, and every L-shape must have exactly 3 '_' characters. The solution involves checking
each '_' cell to see if it can form a valid L-shape with its neighbors, ensuring no '\*' is left unused and no overlapping
L-shapes exist.

problem link: https://codeforces.com/problemset/problem/1722/F

```cpp
#include <bits/stdc++.h>

using namespace std;

const int mod = 1e9 + 7, inf = 2e9;

vector<vector<char>> a;

void solve() {
    int n, m; cin >> n >> m;
    vector<vector<char>> a(n, vector<char>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }
    char s = '*';
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == '.') continue;
            bool f = false;
            if (i - 1 >= 0 && a[i - 1][j] == s) {
                if (j - 1 >= 0 && a[i - 1][j - 1] == s) f = true;
                else if (j + 1 < m && a[i - 1][j + 1] == s) f = true;
            }
            if (i + 1 < n && a[i + 1][j] == s) {
                if (j - 1 >= 0 && a[i + 1][j - 1] == s) f = true;
                else if (j + 1 < m && a[i + 1][j + 1] == s) f = true;
            }
            if (j - 1 >= 0 && a[i][j - 1] == s) {
                if (i - 1 >= 0 && a[i - 1][j - 1] == s) f = true;
                else if (i + 1 < n && a[i + 1][j - 1] == s) f = true;
            }
            if (j + 1 < m && a[i][j + 1] == s) {
                if (i - 1 >= 0 && a[i - 1][j + 1] == s) f = true;
                else if (i + 1 < n && a[i + 1][j + 1] == s) f = true;
            }
            if (i - 1 >= 0 && j - 1 >= 0 && a[i - 1][j] == a[i][j - 1] && a[i - 1][j] == s) f = true;
            if (i + 1 < n && j - 1 >= 0 && a[i + 1][j] == a[i][j - 1] && a[i + 1][j] == s) f = true;
            if (i - 1 >= 0 && j + 1 < m && a[i - 1][j] == a[i][j + 1] && a[i - 1][j] == s) f = true;
            if (i + 1 < n && j + 1 < m && a[i + 1][j] == a[i][j + 1] && a[i + 1][j] == s) f = true;
            //cout << f << ' ' << i << ' ' << j << endl;
            int cnt = 0;
            for (int y = max(0, i - 1); y < min(n, i + 2); y++) {
                for (int x = max(0, j - 1); x < min(m, j + 2); x++) {
                    if (a[y][x] == s) cnt++;
                }
            }
            if (cnt != 3) f = false;
            if (!f) {
                cout << "NO";
                return;
            }
        }
    }
    cout << "YES";
    return;
}

int main() {
    cin.tie(0);
    cin.sync_with_stdio(0);
    int TESTS = 1; cin >> TESTS;
    while (TESTS--) {
        solve();
        cout << '\n';
    }
    return 0;
}
```

