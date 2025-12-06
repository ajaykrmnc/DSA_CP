# Koxia and Number Theory

problem link: https://codeforces.com/problemset/problem/1770/C

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
bool solve(){
    int n;
    cin>>n;
    vector<int>v(n),primes;
    for(int i=0;i<n;i++)cin>>v[i];
    sort(all(v));
    mac(i,1,n){
        if(v[i]==v[i-1])return false;
    }
    for(int i=2;i<60;i++){
        for(int j=2;j<=i;j++){
            if(j==i){
                primes.push_back(i);
            }
            if(i%j==0){
                break;
            }
        }
    }
    for(int j=0;j<primes.size();++j){
        int prime=primes[j];
        vector<int>modulo(prime);
        for(int i=0;i<n;i++){
            modulo[v[i]%prime]++;
        }
        if(*min_element(modulo.begin(),modulo.end())>=2){
            return false;
        }
    }
    return true;
}

int32_t main()
{
    speed()
    int t;
    cin>>t;
    while(t--){
        if(solve()){
            cout<<"YES"<<nline;
        }else 
        cout<<"NO"<<endl;
    }

    return 0;
}
```