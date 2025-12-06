# G - Student Councils

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