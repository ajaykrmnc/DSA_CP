# A- Get Together

problem link:
[Link](https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/A)

There are n people on a straight line, they need to gather at one point. Each person knows his current position 𝑥𝑖 and his speed vi. Help them find out in what minimum time they can gather at one point.

```cpp
#include<bits/stdc++.h>
using namespace std;


#define int long long
#define float double
class solve {
public:
    solve() {
        int n;
        cin >> n;
        vector<pair<int,int>>v(n);
        for(int i = 0; i < n; i++){
            int a, b;
            cin >> a >> b;
            v[i] = {a, b};
        }
        sort(v.begin(), v.end());
        function<bool(float)>pred = [&](float mid){
            vector<pair<float,float>>temp;
            float mini = LLONG_MAX;
            float maxi = -LLONG_MAX;
            for(int i = 0; i < n; i++){
                float pos = v[i].first;
                float speed = v[i].second;
                mini = min(mini, pos + speed * mid);
                maxi = max(maxi, pos - speed * mid);
            }
            if(maxi <= mini){
                return true;
            }
            return false;
        };
        float lo = 0;
        float hi = LLONG_MAX;
        float diff = 0.0000001;
        float ans = -1;
        while(hi-lo >= diff){
            float mid = lo + (hi - lo)/2.0;
            if(!pred(mid)){
                lo = mid + diff;
            }else{
                ans = mid;
                hi = mid - diff;
            }
        }
        cout << fixed << setprecision(10) << ans << endl;
    }
};

```

