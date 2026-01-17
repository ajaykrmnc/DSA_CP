# Parsa Humogous tree

**Problem Statement:**
Given a tree with n nodes, each node can be assigned one of two values from a given range [l_i, r_i]. The goal is to maximize the sum of absolute differences between adjacent nodes. This is a tree DP problem where for each node, you decide which of the two boundary values (l_i or r_i) to assign to maximize the total sum. Use DFS to traverse the tree and maintain DP states for both possible values at each node. The recurrence considers all children and chooses the optimal assignment.

Tags: coloring, graph
problem link: https://codeforces.com/contest/1529/problem/C

```cpp
#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long int ll;
typedef pair<int, int> pii;
 
#define SZ(x)                       (int) x.size()
#define F                           first
#define S                           second
 
const int N = 2e5 + 10;
ll dp[2][N]; int A[2][N], n; vector<int> adj[N];
 
void DFS(int v, int p = -1) {
    dp[0][v] = dp[1][v] = 0;
    for (int u : adj[v]) {
        if (u == p) continue;
        DFS(u, v);
        dp[0][v] += max(abs(A[0][v] - A[1][u]) + dp[1][u], dp[0][u] + abs(A[0][v] - A[0][u]));
        dp[1][v] += max(abs(A[1][v] - A[1][u]) + dp[1][u], dp[0][u] + abs(A[1][v] - A[0][u]));
    }
}
 
void Solve() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%d%d", &A[0][i], &A[1][i]);
    fill(adj + 1, adj + n + 1, vector<int>());
    for (int i = 1; i < n; i++) {
        int u, v; scanf("%d%d", &u, &v);
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    DFS(1);
    printf("%lld\n", max(dp[0][1], dp[1][1]));
}
 
int main() {
    int t; scanf("%d", &t);
    while (t--) Solve();
    return 0;
}
```

```cpp
The problem is equivalent to:
Formal statement: Given a connected graph, paint its edges with several colors so that the edges
of any single color do not make the graph connected, but any 2 colors together make the graph
connected.
This is a constructive problem and there can be a lot of different approaches. We left the limitations
small on purpose, so that you could let your imagination run wild. We will describe a simple solution
which works in time proportional to the size of the input.
How can we make sure the graph is not connected? Take a vertex and remove all incident edges.
So if we paint edges incident to one vertex with color 1 and all other edges with color 2, then color
2 will not connect the graph, while colors 1 and 2 together will connect. And what about color 1
alone? It will connect the graph if and only if the chosen vertex was connected to all of the other
vertices, so if we can find a vertex that is not connected to all of the other vertices, we are done.
Unless the graph is complete, i.e., it contains all possible edges, we can find such a vertex. If, on
the other hand, the graph is complete, we can paint the edges from one vertex with two different
colors (at least one of such edges with one color and at least one of such edges with the other), and
all the other edges with the third color. You can verify that all the conditions are satisfied by this
coloring.
The complexity of this solution is O(n + m).
```