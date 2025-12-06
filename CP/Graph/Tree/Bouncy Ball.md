# Bouncy Ball

problem link: https://codeforces.com/problemset/problem/1807/F

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mydebug.h"
#else
#define debug(x)
#endif

#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define MOD 1000000007
#define inf 1e18
#define ll long long
#define nline "\n"
#define pb push_back
#define set_bits __builtin_popcountll
#define all(x) (x).begin(), (x).end()
void solve()
{
    int n, m, sx, sy, ex, ey;
    cin >> n >> m >> sx >> sy >> ex >> ey;
    string dir;
    cin >> dir;
 
    auto tdir = [](const string& s) {
        return (s[0] == 'U') * 2 + (s[1] == 'L');
    };
 
    auto tid = [&](int x, int y, const string& d) {
        ll z = 1LL * x * m + y;
        return 1LL * tdir(d) * n * m + z;
    };
 
    set<ll> S;
    int B = 0;
    while (1) {
        const auto id = tid(sx, sy, dir);
        if (S.find(id) != S.end()) {
            cout << "-1\n";
            return;
        }
        S.insert(id);
 
        if ((dir == "DL" && ex >= sx && ey <= sy)
            || (dir == "UR" && ex <= sx && ey >= sy)) {
            if (ex + ey == sx + sy) {
                cout << B << '\n';
                return;
            }
        } else if ((dir == "DR" && ex >= sx && ey >= sy)
                   || (dir == "UL" && ex <= sx && ey <= sy)) {
            if (ex - ey == sx - sy) {
                cout << B << '\n';
                return;
            }
        }
 
        if (dir == "DR") {
            int t = min(n - sx, m - sy);
            sx += t;
            sy += t;
        } else if (dir == "DL") {
            int t = min(n - sx, sy - 1);
            sx += t;
            sy -= t;
        } else if (dir == "UR") {
            int t = min(sx - 1, m - sy);
            sx -= t;
            sy += t;
        } else {
            int t = min(sx - 1, sy - 1);
            sx -= t;
            sy -= t;
        }
 
        if (dir[0] == 'D') {
            if (sx == n) {
                dir[0] = 'U';
            }
 
        } else {
            if (sx == 1) {
                dir[0] = 'D';
            }
        }
 
        if (dir[1] == 'L') {
            if (sy == 1) {
                dir[1] = 'R';
            }
 
        } else {
            if (sy == m) {
                dir[1] = 'L';
            }
        }
 
        B++;
    }
}

int32_t main() {
    fastio();
    int t=1;
    cin>>t;
    while(t--){
        solve();
    }

    return 0;

}
```