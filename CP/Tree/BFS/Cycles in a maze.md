# Cycles in a maze

**Problem Statement:**
Given a maze represented as a grid with walls and empty spaces, find if there exists a cycle in the maze. A cycle means
you can start from a cell, move through adjacent empty cells, and return to the starting cell without retracing your path.
Use BFS or DFS to detect cycles in the grid graph. Treat each empty cell as a node and adjacent empty cells as connected.
The key insight is to track parent information during traversal - if you reach a visited cell that is not your immediate
parent, you've found a cycle. Time complexity is O(n*m) where n and m are grid dimensions.

```cpp
#include <bits/stdc++.h>

using namespace std;

int n, m, k;
string s[1007];

bool was[1007][1007];
int min_length[1007][1007];

// Down, Left, Right, Up
int d_row[4] = {1, 0, 0, -1};
int d_col[4] = {0, -1, 1, 0};
char mv[4] = {'D', 'L', 'R', 'U'};

vector<char> ans;

bool can(int row, int column) {
    if (row < 0 || row >= n)
        return false;
    if (column < 0 || column >= m)
        return false;
    if (s[row][column] == '*')
        return false;
    return true;
}

void bfs(int row, int column) {
    queue<pair<int, int>> q;
    queue<int> length;
    q.push(make_pair(row, column));
    length.push(0);

    while (!q.empty()) {
        auto cell = q.front();
        row = cell.first;
        column = cell.second;
        q.pop();
        auto current_length = length.front();
        length.pop();

        if (was[row][column])
            continue;
        was[row][column] = true;
        min_length[row][column] = current_length;

        for (int i=0; i<4; ++i) {
            if (can(row+d_row[i], column+d_col[i]) && !was[row+d_row[i]][column+d_col[i]]) {
                q.push(make_pair(row+d_row[i], column+d_col[i]));
                length.push(current_length + 1);
            }
        }
    }
}

void get_ans(int row, int column) {
    int rest = k;
    while (rest > 0) {
        for (int i=0; i<4; ++i) {
            if (can(row+d_row[i], column+d_col[i]) && min_length[row+d_row[i]][column+d_col[i]] <= rest - 1) {
                ans.push_back(mv[i]);
                row += d_row[i];
                column += d_col[i];
                break;
            }
        }
        --rest;
    }
}

int main() {
    cin >> n >> m >> k;
    for (int i=0; i<n; ++i) {
        cin >> s[i];
    }

    int start_row, start_col;
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j) {
            if (s[i][j] == 'X') {
                start_row = i;
                start_col = j;
            }
        }
    }

    bfs(start_row, start_col);
    get_ans(start_row, start_col);

    if (ans.size() != k) {
        cout << "IMPOSSIBLE";
    } else {
        for (auto c : ans) {
            cout << c;
        }
    }

    return 0;
}
```