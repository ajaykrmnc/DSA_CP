# Even Subarrays

**Problem Statement:**
Given an array of n integers, count the number of subarrays with even XOR. A subarray has even XOR if the XOR of all its elements is even. Use the property that XOR of a range [l,r] equals prefix_xor[r] ⊕ prefix_xor[l-1]. The XOR is even when both prefix XORs have the same parity. Count prefix XORs with even and odd values, then use combinatorial counting to find the answer. The total count is (even_count _ (even_count + 1))/2 + (odd_count _ (odd_count + 1))/2.

problem link: [Link](https://codeforces.com/contest/1731/problem/C)

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

