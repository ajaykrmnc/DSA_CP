# Menorah

**Problem Statement:**
You have two binary strings a and b of length n. You can perform two types of operations: (1) flip any bit in string a,
or (2) swap any two bits in string a. Find the minimum number of operations needed to make string a equal to string b.
The solution involves counting mismatched positions and analyzing different cases: when you can use swaps to fix pairs
of mismatches, or when you need to use flips. Consider the optimal strategy of using swaps first to minimize total operations.

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

