# Longest Simple Cycle

**Problem Statement:**
You have n chains of nodes, where each chain i has c[i] nodes. Adjacent chains are connected by edges with given weights.
Find the longest simple cycle that visits nodes from different chains. A simple cycle cannot repeat nodes or edges.
Use dynamic programming where dp[i][j] represents the longest path ending at node j in chain i that can potentially
form a cycle. The key insight is to track paths that can be extended to form cycles by connecting back to earlier chains.
Consider both continuing existing paths and starting new paths at each chain.

problem link: https://codeforces.com/problemset/problem/1476/C

```cpp
#include <bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mydebug.h"
#else
#define debug(x)
#endif
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
        vector<int>v(n);
        for(auto &x: v){
            cin>>x;
        }
        vector<int>a(n);
        vector<int>b(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        for(int i=0;i<n;i++){
            cin>>b[i];
        }
        int curr=abs(b[1]-a[1])+2;
        int maxi=0;
        debug(t);
        for(int i=1;i<n;i++){
            //
            // debug(curr); 
            maxi=max(curr+v[i]-1,maxi);
            // if not converge
            if(i<n-1)
            if(b[i+1]-a[i+1]==0){
                curr=2;
            }else{
                int tmp=abs(a[i+1]-b[i+1]);
                curr+=(v[i]-tmp+1);
            }
            curr=max(curr,abs(a[i+1]-b[i+1])+2);
            debug(curr);
            debug(maxi);
        }
        cout<<maxi<<nline;
    }

    return 0;
}
```