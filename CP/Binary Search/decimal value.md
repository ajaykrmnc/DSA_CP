# Binary search with decimal

**Problem Statement:**
Given a number n, find the maximum value of x such that x² + √x ≤ n. This is a mathematical optimization
problem that can be solved using binary search on the answer. Since the function f(x) = x² + √x is
monotonically increasing,

```cpp
#include<bits/stdc++.h>
using namespace std;

#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include "mylib/mydebug.h"
#else
#define debug(x)
#endif

#define int long long
#define float double

class solve {
public:
  solve() {
    float n;
    cin >> n;
    function<bool(float)>pred = [&](float x){
      if(x * x + sqrtl(x) <= n){
        return true;
      }
      return false;
    };
    float lo = 0;
    float hi = 1e10;
    float diff = 0.000000001;
    float ans = -1;
    while(hi-lo >= diff){
      float mid = lo + (hi - lo)/2.0;
      if(pred(mid)){
        ans = mid;
        lo = mid + diff;
      }else{
        hi = mid - diff;
      }
    }
    cout << fixed << setprecision(10) << ans << endl;
  }
};

int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL),cout.tie(NULL);
  int t = 1;
  // cin >> t;
  while (t--) {
    solve obj;
  }
  return 0;
}
```
