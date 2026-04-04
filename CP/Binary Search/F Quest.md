# F. Quest

**Problem Statement:**
Given n quests with rewards a_i, you can complete at most one quest per day. After completing a quest, you
cannot do the same quest again for k days. Find the maximum value of k such that you can gain at least c coins
over d days. If impossible, output "Impossible". If k can be arbitrarily large, output "Infinity". This is a
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

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mydebug.h"
#else
#define debug(x)
#endif

#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define MOD 1000000007
#define inf 1e18
#define ll long long
#define nline "\n"
#define pb push_back
#define set_bits __builtin_popcountll
#define all(x) (x).begin(), (x).end()
/*
1 2 3 1
*/
bool check(ll mid,vector<ll>&v,ll c,ll d){
  ll n=v.size();
  ll bucket_size=mid+1;
  ll sum=0;
  for(int i=0;i<min(bucket_size,n);i++){
    sum+=v[i];
  }
  ll tot_bucket=d/bucket_size;
  sum=sum*tot_bucket;
  for(int i=0;i<min(d%bucket_size,n);i++){
    sum+=v[i];
  }
  if(sum>=c){
    return 1;
  }else{
    return 0;
  }
}
int32_t main() {
  fastio();
  int t=1;
  cin>>t;
  while(t--){
    ll n,m,d;
    cin>>n>>m>>d;
    vector<ll>v(n);
    ll sum=0;
    for(auto &x: v){
      cin>>x;
    }
    sort(all(v));
    reverse(all(v));

    // case for infinity
    for(int i=0;i<min(d,n);i++){
      sum+=v[i];
    }
    if(sum>=m){
      cout<<"Infinity"<<nline;
      continue;
    }else if(v[0]*d<m){
      cout<<"Impossible"<<nline;
      continue;
    }
    ll lo=0;
    ll hi=d-2;
    int ans=0;
    while(lo<=hi){
      int mid=lo+(hi-lo)/2;
      if(check(mid,v,m,d)){
        ans=mid;
        lo=mid+1;
      }else{
        hi=mid-1;
      }
    }
    cout<<ans<<nline;

  }

  return 0;

}
```
