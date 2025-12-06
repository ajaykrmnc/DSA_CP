# Multiplicity

problem link: https://codeforces.com/problemset/problem/1061/C

```cpp
#include <bits/stdc++.h>
using namespace std;
#define pb push_back 
#define int long long
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define nline '\n'
#define mac(i,x,y) for(int i=(int)x; i<y; i++)
#define speed() ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
const int mod=1e9+7;
int32_t main()
{
    speed()
    int n;
    cin>>n;
    vector<int>v(n);
    for(int i=0;i<n;i++){
        cin>>v[i];
    }
    vector<vector<int>>div(n);
    int last=1e6;
    vector<int>dp(last+1,0);
    dp[0]=1;
    for(int i=0;i<n;i++){
        for(int j=1;j<=sqrt(v[i]);j++){
            if(v[i]%j==0){
                div[i].pb(j);
                if(j*j!=v[i]){
                    div[i].pb(v[i]/j);
                }
            }
        }
        sort(all(div[i]));
        reverse(all(div[i]));
    }

    for(int i=0;i<n;i++){
        for(auto x: div[i]){
            if(x<=i+1){
                dp[x]+=dp[x-1];
                dp[x]%=mod;
            }
        }
        cout<<nline;
    }
    int ans=0;
    for(int i=1;i<=last;i++){
        if(dp[i]==0){
            break;
        }
        ans+=dp[i];
        ans%=mod;
    }
    cout<<ans<<nline;
    return 0;
}
```