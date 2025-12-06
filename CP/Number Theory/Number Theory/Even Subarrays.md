# Even Subarrays

problem link: https://codeforces.com/contest/1731/problem/C

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

int32_t main()
{
    speed()
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int>v(n);
        for(int i=0;i<n;i++){
            cin>>v[i];
        }
        vector<int>sq;
        for(int i=0;i*i<=5*n;i++){
            sq.pb(i*i);
        }
        vector<int>mp(5*n+1,0);
        int st=0;
        int ans=0;
        int tot=((n*(n+1))/2);
        mp[0]=1;
        for(int i=0;i<n;i++){
            st=(st^v[i]);
            for(auto x: sq){
                int res= (st^x);
                if(res<=5*n){
                    ans+=mp[res];
                }
            }
            mp[st]++;
        }
        cout<<tot-ans<<nline;
    }

    return 0;
}
```