# Menorah

problem link: https://codeforces.com/problemset/problem/1615/C

```cpp
    while(t--){
        int n;
        cin >> n;
        string a, b;
        cin >> a >> b;
 
        int zero, one, one2;
        zero = one = one2 = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] != b[i]) {
                if (a[i] == '0')
                    zero++;
                else
                    one++;
            } else {
                if (a[i] == '1') {
                    one2++;
                }
            }
        }
        int ans = inf;
        if (zero == one) {
            ans = min(ans, 2 * zero);
        }
        if (one2) {
            int zero2 = n - one - zero - one2;
            one2--;
            if (zero2 == one2) {
                ans = min(ans, 2 * zero2 + 1);
            }
        }
        cout << (ans == inf ? -1 : ans) << '\n';
    }

    return 0;

}
```