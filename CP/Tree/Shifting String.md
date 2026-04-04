# Shifting String

```cpp
#include<bits/stdc++.h>
using namespace std;
#define ll long long 

ll LCM(ll x, ll y) { return x * y / __gcd(x, y); }

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        string s;
        cin >> s;

        vector<int> p(n);
        for (int i = 0; i < n; ++i) cin >> p[i], p[i]--;

        ll ans = 1;

        vector<int> vis(n, 0);
        for (int i = 0; i < n; ++i) {
            if (!vis[i]) {
                string cur;
                for (int j = i; !vis[j]; j = p[j]) {
                    vis[j] = 1;
                    cur += s[j];
                }

                // cout << cur << '\n';
                int cnt = 0;
                string t(cur);
                do {
                    rotate(t.begin(), t.begin() + 1, t.end());
                    cnt++;
                } while (t != cur);

                ans = LCM(ans, cnt);
            }
        }
        cout << ans << '\n';
    }

    return 0;
}
```