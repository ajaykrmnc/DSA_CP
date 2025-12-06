# Roads in Berland

```cpp

int main() {
    DIVYA;
#ifndef ONLINE_JUDGE
    freopen("input.txt" , "r" , stdin);
    freopen("output.txt", "w", stdout);
#endif
    ll t, n, i, j, ans, temp, sum;
    string sans;
    t = 1;
    // cin >> t;
    while (t--)
    {
        sans = "NO";
        ans = temp = sum = 0;
        cin >> n;
        vector<vll>dp(n + 1, vll(n + 1, 0));
        fo(i, 1, n)
        {
            fo(j, 1, n)
            {
                cin >> dp[i][j];
            }
        }
        ll k;
        cin >> k;
        while (k--)
        {
            sum = 0;
            ll a, b, c;
            cin >> a >> b >> c;
            fo(i, 1, n)
            {
                fo(j, 1, n)
                {
                    dp[i][j] = min({dp[i][j], dp[i][a] + c + dp[b][j], dp[i][b] + c + dp[a][j]});
                    sum += dp[i][j];
                }
            }
            cout << sum / 2 << " ";
        }
    }
    return 0;
}
```