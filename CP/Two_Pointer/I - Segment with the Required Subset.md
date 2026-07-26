# I - Segment with the Required Subset

**Problem Statement:**
Given an array of n integers, find the shortest segment [l, r] such that there exists a subset of elements within this
segment whose sum equals a target value s. A segment is "good" if you can choose some elements from positions l to r
(inclusive) that sum to exactly s. Use dynamic programming with sliding window optimization to track possible sums for
each segment length and find the minimum length segment that can achieve the target sum.

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mylib/mydebug.h"
#else
#define debug(x)
#endif
#define ll long long
const int mx = INT_MAX;

void solve(){
  int n,sum;
  cin>>n>>sum;
  vector<int>vec(n);
  for(auto &x: vec){
    cin>>x;
  }
  debug(vec);
  vector<pair<int,int>>vis(1005,{0,mx});
  int ans = INT_MAX;
  for(int i = 0; i < n; i++){
    vector<pair<int,int>>new_vis = vis;
    for(int j = 0; j< 1005; j++){
      if(vis[j].second == mx){
        continue;
      }
      int num = vec[i] + j;
      if(num < 1005){
        int temp = vis[j].second+i-vis[j].first;
        if(temp <= vis[num].second){
          new_vis[num].first = i;
          new_vis[num].second = temp;
        }else{
          int temp2 = i - vis[num].first + 1;
          if(num == sum){
            num = min(ans,vis[num].second);
          }
          if(temp <= temp2){
            new_vis[num].first = i;
            new_vis[num].second = temp;
          }
        }
      }
    }
    if(vec[i] < 1005){
      new_vis[vec[i]].first = i;
      new_vis[vec[i]].second = 1;
    }
    swap(new_vis,vis);
    // debug(vis);
  }
  debug(vis);
  if(vis[sum].second == mx){
    cout<<-1<<endl;
    return;
  }else{
    cout<<min(ans,vis[sum].second);
  }
}

int32_t main() {
  int t=1;
  // cin>>t;
  while(t--){
    solve();
  }
  return 0;
}
```

