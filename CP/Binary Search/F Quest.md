# F. Quest

**Problem Statement:**
Given n quests with rewards a_i, you can complete at most one quest per day. After completing a quest, you
cannot do the same quest again for k days. Find the maximum value of k such that you can gain at least c coins
over d days.

If impossible, output "Impossible". If k can be arbitrarily large, output "Infinity". This is a
binary search problem where you need to check if a given k value allows earning enough coins within the time
limit.

problem link: [link](https://codeforces.com/problemset/problem/1760/F)

```cpp

#define int long long

int32_t main() {
  int t;
  cin >> t;
  while (t--) {
    int n, c, d;
    cin >> n >> c >> d;
    vector<int>v(n);
    for(auto &x: v){
      cin >> x;
    }
    debug(v);
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    if(v[0] * d < c){
      cout << "Impossible" << endl;
      continue;
    }
    int sum = 0;
    for(int i = 0; i < min(d, n); i++){
      sum += v[i];
    }
    if(sum >= c){
      cout << "Infinity" << endl;
      continue;
    }
    int lo = 1;
    int hi = 1e9;
    int ans = -1;
    auto pred = [&](int mid){
      int sum = 0;
      for(int i = 0; i < d; i++){
        if((i % mid) >= n){
          sum += 0;
        }else{
          sum += v[i % mid];
        }
      }
      return sum >= c;
    };
    while(lo <= hi){
      int mid = lo + (hi - lo)/2;
      if(pred(mid)){
        ans = mid;
        lo = mid + 1;
      }else{
        hi = mid - 1;
      }
    }
    cout << ans - 1 << endl;
  }
  return 0;
}
```
