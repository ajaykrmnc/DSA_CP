# Hacking Cypher

problem link: https://codeforces.com/contest/490/problem/C

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifndef AJAY
#define debug(x)
#else
#include"mydebug.h"
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#endif

#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define MOD 1000000007
#define ll long long 

#define inf 1e18
#define nline "\n"
#define pb push_back
#define set_bits __builtin_popcountll
#define all(x) (x).begin(), (x).end()

int32_t main() {
    fastio();
    int t=1;
    // cin>>t;
    while(t--){
        string s;
        cin>>s;
        int n=s.size();
        ll a,b;
        cin>>a>>b;
        ll fi=0;
        ll se=0;
        vector<ll>res,res2;
        for(ll i=0;i<s.size();i++){
            fi=fi*10+int(s[i]-'0');
            ll rem=fi%a;
            debug(fi);
            fi%=a;
            debug(rem);
            if(rem==0){res.pb(0);}else res.pb(1);
        }
        ll dus=1;
        reverse(all(s));
        ll f=1;
        for(ll i=0;i<s.size();i++){
            if(s[i]=='0'&&f){
                res2.pb(1);
                dus*=10;
                dus%=b;
                continue;
            }else{
                f=0;
            }
            se=dus*int(s[i]-'0')+se;
            ll rem=se%b;
            dus*=10;
            dus%=b;
            debug(se);
            if(rem==0){res2.pb(0);}else res2.pb(1);
        }
        reverse(all(res2));
        debug(res);
        debug(res2);
        reverse(all(s));
        ll flag=0;
        ll pos=0;
        for(int i=0;i<n-1;i++){
            if(res[i]==0&&res2[i+1]==0){
                flag=1;
                pos=i+1;
                break;
            }
        }
        if(flag){
            cout<<"YES"<<nline;
            for(int i=0;i<pos;i++){
                cout<<s[i];
            }
            while(s[pos]=='0'){
                cout<<s[pos];
                pos++;
            }
            cout<<nline;
            for(int i=pos;i<n;i++){
                cout<<s[i];
            }
        }else{
            cout<<"NO"<<nline;
        }
    }
    return 0;

}
```