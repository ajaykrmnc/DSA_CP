# Path Prefixes

[Problem - 1714G - Codeforces](https://codeforces.com/problemset/problem/1714/G)

```cpp
#include <bits/stdc++.h>

using namespace std;
#define int long long

const int maxn=2e5+5;
vector<int> ch[maxn];
int a[maxn];
int b[maxn];
int ans[maxn];
vector<int> vb;
int curb=0;
int cura=0;

void dfs(int x){
    curb+=b[x];
    cura+=a[x];
    vb.push_back(curb);
    ans[x]=upper_bound(vb.begin(),vb.end(),cura)-vb.begin();
    for(int v:ch[x]){
        dfs(v);
    }
    curb-=b[x];
    cura-=a[x];
    vb.pop_back();
}
int32_t main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    int t;
    cin>>t;
    while(t--){
        int n;cin>>n;
        for(int i=0;i<n;++i) ch[i].clear();
        for(int i=1;i<n;++i){
            int pr,a1,b1;
            cin>>pr>>a1>>b1;
            --pr;
            ch[pr].push_back(i);
            a[i]=a1;
            b[i]=b1;
        }
        dfs(0);
        for(int i=1;i<n;++i) cout<<ans[i]-1<<' ';
        cout<<'\n';
    }
    return 0;
}
```