# All Possible Digits

**Problem Statement:**
Given n digits in base p and a target to make all digits from 0 to p-1 appear at least once, find the minimum number of operations needed. In each operation, you can increment the number by 1. The key insight is to determine whether it's better to increment the current number or to "wrap around" by adding enough to make the most significant digit carry over. Consider two strategies: incrementing until missing digits appear, or incrementing to cause a carry and then finding missing digits in the new configuration.

problem link: https://codeforces.com/problemset/problem/1759/F

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mylib/mydebug.h"
#else
#define debug(x)
#endif
#define ll long long
/*
there will be two cases either we will increase by the unit digit 
// otherwise we will have too increase the 2nd digit 
// so we have the data of other's digits
// what we can do maximum unachievable number in unit digit
// if we are closer to achieving 0 then like greater than 1/2 of the digits passed
// otherwise we are closer to 0 
// if we are close to 0 and unit digit is greater than 0 then minimum unachievable is something we have to consider
// if like unit digit is greater than 0 then ans will be from p t
*/
class solve{
    public:
    solve(){
        int n,p;
        cin >> n >> p;
        set<int>st;
        vector<int>v(n);
        for(int i = 0; i < n; i++){
            cin >> v[i];
            st.insert(v[i]);
        }
        // if(v[n-1] == 0){
        //     for(int i = p - 1; i >=0; i--){
        //         if(st.find(i) == st.end()){
        //             cout << i << endl;
        //             return;
        //         }
        //     }
        //     cout << 0 << endl;
        //     return;
        // }
        // there will be two situation either we have to achieve beyond 2 to 0 then 1 or we can find the integers as incresed 
        // to zero

        // case 1
        if(st.size() == p){
            cout << 0 << endl;
            return;
        }
        int flag = 0;
        for(int i = v[n - 1] - 1; i >= 0; i--){
            if(st.find(i) == st.end()){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            for(int i = p - 1; i > v[n - 1]; i--){
                if(st.find(i) == st.end()){
                    cout << i - v[n - 1] << endl;
                    return;
                }
            }
            cout << 0;
            return;
        }
        int carry = 1;
        for(int i = n - 2;i >=0; --i){
            st.insert(v[i] + carry);
            carry = (v[i] + carry)/p;
        }
        debug(carry);
        if(carry == 1){
            st.insert(1);
        }
        int req = 0;
        for(int i = v[n - 1] - 1; i > 0; i--){
            if(st.find(i) == st.end()){
                req = i;
                break;
            }
        }
        cout << p - v[n - 1] + req << endl;

    }
};

int32_t main() {
    int t=1;
    cin>>t;
    while(t--){
        solve obj;
    }
    return 0;
}
```