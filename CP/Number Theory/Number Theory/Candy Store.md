# Candy Store

**Problem Statement:**
Given n candies with prices (a[i], b[i]) where you pay a[i] coins and get b[i] candies, find the minimum number of days needed to buy all candies such that on each day the ratio of total coins spent to total candies received is an integer. This problem involves number theory concepts like GCD and LCM. For each day, maintain the cumulative ratio and check if it remains integral. Use GCD to simplify fractions and determine when ratios become non-integral, requiring a new day to start.

problem link: https://codeforces.com/contest/1798/problem/C

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
        vector<pair<int,int>>v(n);
        for(int i=0;i<n;i++){
            int a,b;
            cin>>a>>b;
            v[i]={a,b};
        }
        int cnt=n;
        int curr=-1;
        int curr_mini=0,curr_maxi=0;
        for(int i=0;i<n;i++){
            auto [p,q]=v[i];
            if(curr!=-1){
                int gcd=__gcd(curr_mini,q);
                curr_mini=((curr_mini*q)/gcd);
                curr_maxi=__gcd(curr_maxi,p*q);
                if((curr_maxi%curr_mini)==0){
                    cnt--;
                }else{
                    curr=-1;
                }
            }
            if(curr==-1){
                curr_mini = q;
                curr_maxi = p*q;
                curr=1;
            }
        }
        cout<<cnt<<nline;
    }

    return 0;
}
```

Candy Store