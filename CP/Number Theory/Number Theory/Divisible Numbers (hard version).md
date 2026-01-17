# Divisible Numbers (hard version)

**Problem Statement:**
Given four integers a, b, c, d, find two integers x and y such that a < x ≤ b, c < y ≤ d, and x*y is divisible by a*c. The hard version has larger constraints requiring efficient algorithms. The key insight is to iterate through divisors of a*c and for each divisor, check if valid x and y can be found. Use mathematical properties to optimize the search and handle large numbers efficiently. Consider factorization and divisor enumeration techniques.

problem link: https://codeforces.com/problemset/problem/1744/E2

```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

int32_t main()
{
    ios_base::sync_with_stdio(NULL);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin>>t;
    while(t--){
        int a,b,c,d;
        cin>>a>>b>>c>>d;

        vector<int> diva,divb;
        set<int> div;

        for(int i=1;i*i<=a;i++){
            if(a%i==0){
                diva.push_back(i);
                if(a/i != i){
                    diva.push_back(a/i);
                }
            }
        }

        for(int i=1;i*i<=b;i++){
            if(b%i==0){
                divb.push_back(i);
                if(b/i != i){
                    divb.push_back(b/i);
                }
            }
        }

        for(int i=0;i<diva.size();i++){
            for(int j=0;j<divb.size();j++){
                div.insert(diva[i]*divb[j]);
            }
        }

        int x=-1,y=-1;
        for(auto ele:div){
            int tmp=a*b/ele;
            if(d/ele > b/ele && c/tmp > a/tmp){
                x=tmp*(c/tmp);
                y=ele*(d/ele);
                break;
            }
            if(d/tmp > b/tmp && c/ele > a/ele){
                x=ele*(c/ele);
                y=tmp*(d/tmp);
                break;
            }
        }

        cout<<x<<" "<<y<<endl;
    }
    return 0;
 }
```