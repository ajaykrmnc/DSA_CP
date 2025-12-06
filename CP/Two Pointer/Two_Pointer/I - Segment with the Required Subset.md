# I - Segment with the Required Subset

```cpp
Given an array of 𝑛 integers 𝑎𝑖. Let's say that a segment of this array 𝑎[𝑙..𝑟]
is good if on this segment it is possible to choose a certain set of numbers whose sum is equal to 𝑠
Your task is to find the shortest good segment.
```

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