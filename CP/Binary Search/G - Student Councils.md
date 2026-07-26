# G - Student Councils

**Problem Statement:**
You need to form student councils where each council has exactly k members. You have n groups of students with a_i
students in the i-th group. From each group, you can select at most x students for all councils combined. Find the
maximum number of complete councils you can form.

This is a binary search problem where you binary search on the answer
(number of councils) and check if it's possible to form that many councils given the constraints.

Problem link: [AtCoder Educational DP Contest](https://atcoder.jp/contests/dp)

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

class solve {
public:
  solve() {
    int k, n;
    cin >> k >> n;
    vector<int>v(n);
    for(int i = 0; i < n; i++){
      cin >> v[i];
    }
    function<bool(int)>pred = [&](int mid){
      int sum = 0;
      for(int i = 0; i < n; i++){
        sum += min(v[i], mid);
      }
      if(sum / k >= mid){
        return true;
      }
      return false;
    };

    sort(v.begin(), v.end());
    int lo = 1;
    int hi = LLONG_MAX;
    int ans = -1;
    while(lo <= hi){
      int mid = lo + (hi - lo)/2;
      if(pred(mid)){
        ans = mid;
        lo = mid + 1;
      }else{
        hi = mid - 1;
      }
    }
    cout << ans << endl;
  }
};

int32_t main() {
  int t = 1;
  // cin >> t;
  ios_base::sync_with_stdio(false);
  cin.tie(NULL),cout.tie(NULL);
  while (t--) {
    solve obj;
  }
  return 0;
}
```

