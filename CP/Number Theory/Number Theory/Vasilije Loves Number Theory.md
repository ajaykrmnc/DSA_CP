# Vasilije Loves Number Theory

problem link: https://codeforces.com/problemset/problem/1878/F

Vasilije is a smart student and his discrete mathematics teacher Sonja taught
him number theory very well.

He gave Ognjen a positive integer 𝑛
. Denote 𝑑(𝑛) as the number of positive integer divisors of 𝑛
, and denote 𝑔𝑐𝑑(𝑎,𝑏) as the largest integer 𝑔 such that 𝑎 is divisible by 𝑔
and 𝑏 is divisible by g.

After that, he gave Ognjen 𝑞 queries, and there are 2 types of queries. 1
, 𝑥 — set 𝑛 to 𝑛⋅𝑥 , and then answer the following question: does there exist a positive integer such that 𝑔𝑐𝑑(𝑎,𝑛)=1
, and 𝑑(𝑛⋅𝑎)= n? 2— reset 𝑛
to its initial value (before any queries).
Note that 𝑛
does not get back to its initial value after the type 1 query.

Since Ognjen is afraid of number theory, Vasilije promised him that after each query, 𝑑(𝑛)≤109
, however, even with that constraint, he still needs your help with this problem.

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mylib/mydebug.h"
#else
#define debug(x)
#endif
#define int long long

int binexp(int n,int p){
    int ans = 1;
    int st = 1;
    while(p > 0){
        st *= n;
        if(p % 2 == 1){
            ans *= st;
        }
        p/=2;
    }
    return ans;
}
int powersum(int n,int p){
    int ans = 0;
    for(int i = 1; i <=p; i++){
        ans+=(binexp(n,i));
    }
    return ans;
}

const int sizee=1e6+10;
int spf[sizee];
vector<int>primes;
void sieve(){
   for(int i=0;i<sizee;i++)
      spf[i]=i;

   for(int i=2;i*i<sizee;i++){
      if(spf[i]==i){
         for(int j=i*i;j<sizee;j+=i){
            if(spf[j]==j)
               spf[j]=i;
         }
      }
   }
   for(int i=2;i<sizee;i++){
        if(spf[i]==i){
            primes.push_back(i);
        }
    }
}

class solve{
    public:
    solve(){
        int n, q;
        cin >> n >> q;
        map<int,int>mp;
        int num = n;
        while(num > 1){
            mp[spf[num]]++;
            num/=spf[num];
        }
        int st,d = 1;
        map<int,int>divd,initdivd;
        for(auto [x,cnt]: mp){
            int num = cnt + 1;
            while(num > 1){
                divd[spf[num]]++;
                num/=spf[num];
            }
        }
        initdivd = divd;
        for(int i = 0; i < q; i++){
            int a;
            cin >> a;
            if(a == 2){
                int num = n;
                mp.clear();
                while(num > 1){
                    mp[spf[num]]++;
                    num/=spf[num];
                }
                divd = initdivd;
                continue;
            }
            int ex;
            cin >> ex;
            map<int,int>divex;
            while(ex > 1){
                divex[spf[ex]]++;
                ex /= spf[ex];
            }
            for(auto [x,cnt]: divex){
                int num;
                if(mp.find(x) == mp.end()){
                    mp[x] = cnt;
                    num = cnt + 1;
                }else{
                    num = mp[x] + 1;
                    while(num > 1){
                        divd[spf[num]]--;
                        if(divd[spf[num]] == 0){
                            divd.erase(spf[num]);
                        }
                        num/=spf[num];
                    }

                    num = mp[x] + cnt + 1;
                    mp[x] += cnt;
                }
                while(num > 1){
                    divd[spf[num]]++;
                    num /= spf[num];
                }
            }
            int flag = 1;
            debug(divd);
            debug(mp);
            for(auto [x,cnt]: divd){
                if(mp.find(x) == mp.end()){
                    flag = 0;
                    break;
                }
                if(mp[x] < cnt){
                    flag = 0;
                    break;
                }
            }
            if(flag == 0){
                cout << "NO" << endl;
            }else{
                cout << "YES" << endl;
            }
        }
        cout << endl;
    }
};

int32_t main() {
    int t=1;
    cin>>t;
    sieve();
    // cout << binexp(2,3);
    while(t--){
        solve obj;
    }
    return 0;
}
```

