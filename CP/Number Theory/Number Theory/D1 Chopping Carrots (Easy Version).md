# D1. Chopping Carrots (Easy Version)

problem link: https://codeforces.com/contest/1706/problem/D1

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
#define ll long long
#define nline "\n"
#define pb push_back
#define set_bits __builtin_popcountll
#define all(x) (x).begin(), (x).end()
vector<vector<int>>factors(3005);
void solve(){
    for(int i=1;i<3005;i++){
        factors[i].pb(i);
        for(int j=2;j<3005;j++){
            if(i/j!=factors[i].back()){
                factors[i].pb(i/j);
            }
        }
        reverse(factors[i].begin(),factors[i].end());
    }
}
const int inf=INT_MAX;
int32_t main() {
    fastio();
    int t=1;
    cin>>t;
    solve();
    // debug(factors);
    while(t--){
        int n,k;
        cin>>n>>k;
        vector<int>v(n);
        for(auto &x: v){
            cin>>x;
        }
        sort(all(v));
        // debug(v);
        vector<int>dp(3005,inf);
        for(int i=0;i<n;i++){
            vector<int>tmp(3005,inf);
            auto it=lower_bound(factors[v[i]].begin(),factors[v[i]].end(),v[i]/k);
            if(i==0){
                while(it!=factors[v[i]].end()){
                    tmp[*it]=0;
                    it++;
                }
            }else{
                 while(it!=factors[v[i]].end()){
                    int num = *it;
                    debug(num);
                    for(int j=1;j<3005;j++){
                        if(dp[j]!=inf){
                            int res=dp[j];
                            int maxi=max(res+j,num);
                            int mini=min(j,num);
                            tmp[mini]=min(maxi-mini,tmp[mini]);
                        }
                    }
                    it++;
                }
            }
            // debug(dp[i]);
            dp=tmp;
        }
        int ans=inf;
        for(int j=0;j<3005;j++){
            ans=min(ans,dp[j]);
        }
        cout<<ans<<nline;
        debug(ans);

    }

    return 0;

}
```