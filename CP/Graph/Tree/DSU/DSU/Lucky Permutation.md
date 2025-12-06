# Lucky Permutation

[Problem - 1768D - Codeforces](https://codeforces.com/problemset/problem/1768/D)

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
    vector<int>e;
    dsu(int n): e(n,-1) {}
    bool sameSet(int a,int b){ return find(a)==find(b);}
    int find(int x){ return e[x]<0 ? x: e[x]=find(e[x]);}
    int size(int x){ return -e[find(x)];}
    bool join(int a,int b){
        a= find(a),b=find(b);
        if(a==b){
            return false;
        }
        if(e[a]>e[b]) swap(a,b);
        e[a]+=e[b];e[b]=a;
        return true;
    }
};
bool solve(){
    int n;
    cin>>n;
    vector<int>v(n);
    mac(i,0,n){
        cin>>v[i];
    }
    dsu d(n);
    for(int i=0;i<n;i++){
        v[i]--;
        d.join(i,v[i]);
    }
    int cycles=0;
    set<int>s;
    for(int i=0;i<n;i++){
        s.insert(d.find(i));
    }
    cycles=s.size();
    for(int i=0;i<n-1;i++){
        if(d.sameSet(v[i],v[i+1])){
            cout<<n-(cycles+1)<<endl;
            return true;
        }
    }
    cout<<(n-cycles+1)<<endl;
    return true;

}

int32_t main()
{
    speed()
    int t;
    cin>>t;
    while(t--){
        if(solve()){
            // cout<<"YES"<<endl;
        }else {
            // cout<<"NO"<<endl;
        }
    }

    return 0;
}
```