# Minimum Cost string

**Problem Statement:**
Given integers n and k, construct a string of length n using the first k letters of the alphabet such that the number of distinct substrings is minimized. The key insight is to use Eulerian path in a De Bruijn graph. Create a directed graph where each node represents a string of length (k-1), and edges represent adding one character. Find an Eulerian path that visits each edge exactly once. This generates the lexicographically smallest string with minimum distinct substrings. Use DFS to traverse the graph and construct the optimal string.

problem link: https://codeforces.com/contest/1511/problem/D

```cpp
#include <bits/stdc++.h>

using namespace std;

int n, k;
int cur[26];
vector<int> path;

void dfs(int v) {
  while (cur[v] < k) {
    int u = cur[v]++;
    dfs(u);
    path.push_back(u);
  }
}

int main() {
  scanf("%d%d", &n, &k);
  dfs(0);
  printf("a");
  for (int i = 0; i < n - 1; ++i)
    printf("%c", path[i % path.size()] + 'a');
}
```