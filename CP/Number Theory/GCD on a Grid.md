# GCD on a Grid

problem link: [Link Url](https://codeforces.com/contest/1955/problem/G)

```cpp
#include <bits/stdc++.h>
using namespace std;

#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include "mylib/mydebug.h"
#else
#define debug(x)
#endif

// #define int long long

void solve() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }
    int gcd = __gcd(matrix[n - 1][m - 1], matrix[0][0]);
    vector<int> factors;
    for (int i = 1; i * i <= gcd; i++) {
        if (gcd % i == 0) {
            factors.push_back(i);
            if (i != gcd / i) factors.push_back(gcd / i);
        }
    }
    int maxi = 1;
    for (auto &x : factors) {
        int num = x;
        int vis[n][m];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                vis[i][j] = 0;
            }
        }
        vis[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0) continue;
                if(matrix[i][j] % num > 0) continue;
                if (i > 0 && vis[i - 1][j] == 1) vis[i][j] = 1;
                if (j > 0 && vis[i][j - 1] == 1) vis[i][j] = 1;
            }
        }
        if(vis[n - 1][m - 1]){
            maxi = max(maxi, x);
        }
    }
    cout << maxi << endl;
}

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}

```

