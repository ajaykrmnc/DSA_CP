# Buying Gifts

```cpp
Little Sasha has two friends, whom he wants to please with gifts on the Eighth 
of March. To do this, he went to the largest shopping center in the city.
There are 𝑛 departments in the mall, each of which has exactly two stores. For convenience, we number the departments with integers from 1
 to 𝑛. It is known that gifts in the first store of the 𝑖 department cost 𝑎𝑖
 rubles, and in the second store of the 𝑖 department — 𝑏𝑖 rubles.

Entering the mall, Sasha will visit each of the 𝑛 departments of the mall, and in each department, he will enter exactly one store. When Sasha gets into the 𝑖-th department, he will perform exactly one of two actions:

Buy a gift for the first friend, spending 𝑎𝑖  rubles on it.
Buy a gift for the second friend, spending 𝑏𝑖 rubles on it.
Sasha is going to buy at least one gift for each friend. Moreover, he wants to pick up gifts in such a way that the price difference of the most expensive gifts bought for friends is as small as possible so that no one is offended.

More formally: let 𝑚1
  be the maximum price of a gift bought to the first friend, and 𝑚2
  be the maximum price of a gift bought to the second friend. Sasha wants to choose gifts in such a way as to minimize the value of |𝑚1−𝑚2|
.
```

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
#define inf LLONG_MAX
int32_t main()
{
    speed()
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<pair<int,int>>pii(n);
        for(int i=0;i<n;i++){
            int a,b;
            cin>>a>>b;
            pii[i]={a,b};
        }
        sort(all(pii));
        vector<int>suf(n+1);
        suf[n]=0;
        for(int i=n-1;i>=0;i--){
            suf[i]=max(pii[i].second,suf[i+1]);
        }
        set<int>st;
        int ans=inf;
        for(int i=0;i<n;i++){
            if(i==n-1){
                int res=inf;
                auto it=st.upper_bound(pii[i].first);
                if(it!=st.end()){
                    res=min(abs(*it-pii[i].first),res);
                }
                {
                    if(it!=st.begin()){
                        it--;
                        res=min(abs(*it-pii[i].first),res);
                    }
                }
                ans=min(ans,res);
                continue;
            }
            int res=abs(suf[i+1]-pii[i].first);
            if(suf[i+1]>=pii[i].first){
                res=res;
            }else{
                auto it=st.upper_bound(pii[i].first);
                if(it!=st.end()){
                    res=min(abs(*it-pii[i].first),res);
                }
                {
                    if(it!=st.begin()){
                        it--;
                        if(*it>=suf[i+1]){
                            res=min(abs(*it-pii[i].first),res);
                        }
                    }
                }
            }
            st.insert(pii[i].second);
            ans=min(ans,res);
        }
        cout<<ans<<nline;

    }

    return 0;
}
```
