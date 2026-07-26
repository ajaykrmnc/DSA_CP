# Natalan Exploring

**Problem Statement:**
Given an array of n integers, find the number of ways to choose a subsequence such that the product of GCD of all pairs
in the subsequence equals the LCM of all elements in the subsequence.

This is an advanced number theory problem
requiring deep understanding of GCD, LCM properties, and prime factorization. Use inclusion-exclusion principle and
mathematical analysis of prime factor contributions. The solution involves complex combinatorial counting with modular
arithmetic.

problem link: https://codeforces.com/contest/2037/problem/G

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX_VAL = 1e6 + 1;
const int MOD = 998244353;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> arr(n);
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  vector<int> spf(MAX_VAL); // Smallest Prime Factor
  for (int i = 0; i < MAX_VAL; i++) {
    spf[i] = i;
  }
  for (int i = 2; i * i < MAX_VAL; i++) {
    if (spf[i] == i) {
      for (int j = i * i; j < MAX_VAL; j += i) {
        if (spf[j] == j) {
          spf[j] = i;
        }
      }
    }
  }
  vector<ll> sumMult(MAX_VAL, 0);
  ll result = 0;
  for (int i = 0; i < n; i++) {
    ll dpVal = 0;
    if (i == 0) {
      dpVal = 1;
    } else {
      vector<int> primes;
      int x = arr[i];

      while (x > 1) {
        int p = spf[x];
        primes.push_back(p);

        while (x % p == 0) {
          x /= p;
        }
      }

      int cnt = primes.size();
      if (cnt == 0) {
        dpVal = 0;
      } else {
        ll incExcSum = 0;

        for (int mask = 1; mask < (1 << cnt); mask++) {
          int prod = 1, bits = 0;

          for (int j = 0; j < cnt; j++) {
            if (mask & (1 << j)) {
              prod *= primes[j];
              bits++;
            }
          }

          if (bits % 2 == 1) {
            incExcSum = (incExcSum + sumMult[prod]) % MOD;
          } else {
            incExcSum = (incExcSum - sumMult[prod] + MOD) % MOD;
          }
        }

        dpVal = incExcSum;
      }
    }

    if (i == n - 1) {
      result = dpVal;
    }

    vector<int> updatePrimes;
    int y = arr[i];

    while (y > 1) {
      int p = spf[y];
      updatePrimes.push_back(p);

      while (y % p == 0) {
        y /= p;
      }
    }

    int m = updatePrimes.size();
    for (int mask = 1; mask < (1 << m); mask++) {
      int prod = 1;

      for (int j = 0; j < m; j++) {
        if (mask & (1 << j)) {
          prod *= updatePrimes[j];
        }
      }

      sumMult[prod] = (sumMult[prod] + dpVal) % MOD;
    }
  }

  cout << result << "\n";
  return 0;
}
```

