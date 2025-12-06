# Count GCD

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

const int mod=998244353;

int inclusion(int prev,int next,int m){
    int res=m/next;
    int mul=m/next;
    vector<int>need;
    int x=prev/next;
    for(int i=2;i*i<=x;i++){
        if(x%i==0){
            while(x%i==0){
                x/=i;
            }
            need.pb(i);
        }
    }
    if(x>1){
        need.pb(x);
    }
    int sz=need.size();
    for(int mask=1;mask<(1ll<<sz);mask++){
        int temp=1;
        for(int i=0;i<sz;i++){
            if(mask&(1ll<<i)){
                temp*=need[i];
            }
        }
        if(__builtin_parity(mask)){
            res-=(mul/temp);
        }else{
            res+=(mul/temp);
        }
    }
    return res;
}
int32_t main()
{
    speed()
    int tt;
    cin>>tt;
    while(tt--){
        int n,m;
        cin>>n>>m;
        vector<int>v(n);
        mac(i,0,n){
            cin>>v[i];
        }
        int ans=1;
        int flag=0;
        mac(i,1,n){
            if(v[i-1]%v[i]){
                flag=1;
                break;
            }else{
                ans*=(inclusion(v[i-1],v[i],m));
                ans%=mod;
            }
        }
        if(flag){
            cout<<0<<nline;
        }else 
        cout<<ans<<nline;
    }

    return 0;
}
```