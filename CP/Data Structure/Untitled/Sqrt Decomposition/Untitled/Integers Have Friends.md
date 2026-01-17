# Integers Have Friends

**Problem Statement:**
Given an array of n integers, find the maximum length of a subarray where all pairwise GCDs are greater than 1. This means
for any two elements in the chosen subarray, their GCD should be at least 2. The problem can be solved using sqrt decomposition
or segment tree with GCD operations. The key insight is that if all pairwise GCDs in a subarray are > 1, then the GCD of
the entire subarray is also > 1. Use binary search on the answer length and check if a subarray of that length exists
with the required property. Time complexity is O(n log n log(max_value)).

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vb = vector<bool>;
using vvb = vector<vb>;
using vi = vector<int>;
using vvi = vector<vi>;
using vl = vector<ll>;
using vvl = vector<vl>;
using vc = vector<char>;
using vvc = vector<vc>;
using vs = vector<string>;
const ll mod = 1e9 + 7,inf = 1e18;
#define pb push_back
#define fast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
void setIO()
{
    fast;
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
}

int main()
{
    setIO();
    int t;
    cin>>t;

    while (t--){
        int n;
        cin>>n;
        vl a(n + 1),b(n + 1);
        for (int i = 1;i<=n;i++)
            cin>>a[i];
        
        for (int i = 1;i<=n;i++)
            b[i] = a[i] - a[i - 1];

        vvl table(n + 1,vl(21));
        
        for (int i = 1;i<=n;i++)
            table[i][0] = b[i];

        for (int j = 1;j<=20;j++){
            for (int i = 1;i + (1<<j) <= n + 1;i++){
                table[i][j] = __gcd(table[i][j - 1],
                    table[i + (1<<(j - 1))][j - 1]);
            }
        }

        int l = 1,r = n,ans = 1;
        
        while (l <= r){
            int mid = (l + r)/2;
            bool is = false;

            for (int i = 1;i<=n - mid + 1;i++){
                    
                int l = i + 1,r = i + mid - 1;
                ll val = b[l];

                for (int j = 20;j>=0;j--){
                    if ((1<<j) <= r - l + 1){
                        val = __gcd(val,table[l][j]);
                        l += (1<<j);
                    }
                }
                if (abs(val) > 1 or val == 0){is = true;break;}
            }   
            if (is){
                ans = mid;
                l = mid + 1;
            }
            else r = mid - 1;
        }
        cout<<ans<<'\n';
    }
    return 0;
}
```