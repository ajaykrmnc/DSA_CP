# Array differentiation

problem link: https://codeforces.com/problemset/problem/1552/D

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
        int sz=n;
        int tot=(1<<sz);
        set<int>st;
        for(int mask=0;mask<tot;mask++){
            int sum=0;
            for(int i=0;i<sz;i++){
                if((mask&(1<<i))){
                    sum+=v[i];
                }
            }
            st.insert(sum);
        }
        if(st.size()==tot){
            cout<<"NO"<<nline;
        }else{
            cout<<"YES"<<nline;
        }
        
    }

    return 0;
}
```