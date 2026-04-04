# Nastya and Potions

Tags: kahn

```cpp
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  cin >> tt;
  while (tt--) {
    int n, k;
    cin >> n >> k;
    vector<int> c(n);
    for (int i = 0; i < n; i++) {
      cin >> c[i];
    }
    for (int i = 0; i < k; i++) {
      int x;
      cin >> x;
      --x;
      c[x] = 0;
    }
    vector<vector<int>> graph(n);
    vector<int> deg(n);
    vector<vector<int>> need(n);
    for (int i = 0; i < n; i++) {
      cin >> deg[i];
      need[i].resize(deg[i]);
      for (int j = 0; j < deg[i]; j++) {
        cin >> need[i][j];
        --need[i][j];
        graph[need[i][j]].push_back(i);
      }
    }
    vector<int> que;
    for (int i = 0; i < n; i++) {
      if (deg[i] == 0) {
        que.push_back(i);
      }
    }
    for (int b = 0; b < (int) que.size(); b++) {
      for (int u : graph[que[b]]) {
        deg[u] -= 1;
        if (deg[u] == 0) {
          que.push_back(u);
        }
      }
    }
    assert((int) que.size() == n);
    for (int i : que) {
      if (!need[i].empty()) {
        int s = 0;
        for (int j : need[i]) {
          s += c[j];
          if (s > c[i]) {
            break;
          }
        }
        c[i] = min(c[i], s);
      }
    }
    for (int i = 0; i < n; i++) {
      cout << c[i] << " \n"[i == n - 1];
    }
  }
  return 0;
}
```

[Problem - 1851E - Codeforces](https://codeforces.com/problemset/problem/1851/E)