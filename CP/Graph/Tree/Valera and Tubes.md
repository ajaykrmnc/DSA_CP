# Valera and Tubes

problem link: https://codeforces.com/contest/441/problem/C

```cpp
#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define int long long
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define nline '\n'
#define mac(i, x, y) for (int i = (int)x; i < y; i++)
#define speed() ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
pair<int, int> coord(int a, int m)
{
    int y = a / m;
    int x = a % m;
    pair<int, int> pi;
    if ((a / m) % 2 == 0)
    {
        pi.first = x + 1;
        pi.second = y + 1;
        return pi;
    }
    else
    {
        pi.first = m - x;
        pi.second = y + 1;
        return pi;
    }
}

int32_t main()
{
    speed()
    int n, m, r;
    cin >> n >> m >> r;
    int res = 0;
    for (int i = 0; i < r - 1; i++)
    {
        cout<<2<<' ';
        for (int j = 0; j < 2; j++)
        {
            pair<int, int> pi = coord(res + j, m);
            cout << pi.second << " " << pi.first<<" ";
        }
        res += 2;
        cout<<nline;
    }
    cout<<n*m-res<<" ";
    for(int i=res;i<n*m;i++)
    {
        pair<int, int> pi = coord(i, m);
        cout << pi.second << " " << pi.first<<" ";

    }
    cout<<nline;

    return 0;
}
```