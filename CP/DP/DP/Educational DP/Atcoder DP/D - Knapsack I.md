# D - Knapsack I

```cpp
#include <bits/stdc++.h>
using namespace std;

#define pb push_back 
#define int long long
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define nline '\n'
#define mac(i,x,y) for(int i = (int)x; i < y; i++)
#define speed() ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);

const int N = 1000005;
int vec[N][2];
int dp[101][100005];

int fun(int i, int m) {
    if (i < 0)
        return 0;
    if (dp[i][m] != -1)
        return dp[i][m];
    int w = vec[i][0];
    int v = vec[i][1];
    if (m - w < 0)
        return dp[i][m] = fun(i - 1, m);

    int maxi = max(v + fun(i - 1, m - w), fun(i - 1, m));

    return dp[i][m] = maxi;
}

int32_t main() {
    speed();
    memset(dp, -1, sizeof(dp));
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> vec[i][0] >> vec[i][1];
    }
    cout << fun(n - 1, m) << nline;

    return 0;
}

```