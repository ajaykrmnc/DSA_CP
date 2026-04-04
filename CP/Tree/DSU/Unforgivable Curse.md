# Unforgivable Curse

problem link: https://codeforces.com/contest/1800/problem/E2

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
struct dsu{
    vector<int>count,pred;
    dsu(int n){
        count.resize(n,1);
        pred.resize(n);
        for(int i=0;i<n;i++){
            pred[i]=i;
        }
    }
    int get(int p){
        if(pred[p]!=p){
            pred[p]=get(pred[p]);
        }
        return pred[p];
    }
    bool check(int a,int b){
        return get(a)==get(b);
    }
    void merge(int a,int b){  
        a=get(a);
        b=get(b);
        if(count[a]>count[b]){   // b for bada
            swap(a,b);
        }
        pred[a]=pred[b];
        count[a]+=count[b];
    }
};

int32_t main()
{
    speed()
    int tt;
    cin>>tt;
    while(tt--){
        int n,k;
        cin>>n>>k;
        string s,t;
        cin>>s>>t;
        dsu d(n);
        for(int i=0;i<n;i++){
            if(i+k<n)
            d.merge(i,i+k);
            if(i+k+1<n){
                d.merge(i,i+k+1);
            }
        }
        map<int,vector<int>>mp;
        for(int i=0;i<n;i++){
            mp[d.get(i)].pb(i);
        }
        int flag=1;
        for(auto [root,vec]: mp){
            multiset<char>mst,mst2;
            for(auto x: vec){
                mst.insert(s[x]);
            }
            for(auto x: vec){
                mst2.insert(t[x]);
            }
            if(mst!=mst2){
                flag=0;
            }
        }
        if(flag){
            cout<<"YES"<<nline;
        }else{
            cout<<"NO"<<nline;
        }
    }

    return 0;
}
```