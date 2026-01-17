# Apple Man tree

**Problem Statement:**
Given a tree with n nodes where each node is either black or white, count the number of ways to remove some edges such that all remaining black nodes are in one connected component and all white nodes are in separate connected components (each white node forms its own component). This is a tree DP problem where you need to consider the state of each subtree. For each node, calculate the number of ways considering whether the subtree rooted at that node contributes to the main black component or forms separate components.

problem link: https://codeforces.com/problemset/problem/461/B

![Untitled](Apple%20Man%20tree/Untitled.png)

![Untitled](Apple%20Man%20tree/Untitled%201.png)

![Untitled](Apple%20Man%20tree/Untitled%202.png)

![Untitled](Apple%20Man%20tree/Untitled%203.png)

![Untitled](Apple%20Man%20tree/Untitled%204.png)

![Untitled](Apple%20Man%20tree/Untitled%205.png)

```cpp
/*
*   author: kartik8800
*/

#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define fr(a,b) for(int i = a; i < b; i++)
#define rep(i,a,b) for(int i = a; i < b; i++)
#define mod 1000000007
#define inf (1LL<<60)
#define all(x) (x).begin(), (x).end()
#define prDouble(x) cout << fixed << setprecision(10) << x
#define triplet pair<ll,pair<ll,ll>>
#define goog(tno) cout << "Case #" << tno <<": "
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
#define int long long
using namespace std;

vector<int> tree[100001];
bool blackColor[100001];
int dp_white[100001], dp_black[100001];

void solve(int root, int par){

    for(int child: tree[root])
        if(child != par)
            solve(child, root);

    if(blackColor[root]){
        dp_white[root] = 0;
        ll blackComps = 1;
        for(int child: tree[root]){
            if(child != par)
                blackComps = (blackComps * (dp_white[child] + dp_black[child])) % mod;
        }
        dp_black[root] = blackComps;
    }
    else{
        vector<int> pref, suf, nodeWhiteVal, nodeBlackVal;

        for(int child: tree[root])
            if(child != par){
                nodeWhiteVal.push_back(dp_white[child]);
                nodeBlackVal.push_back(dp_black[child]);
            }

        if(nodeWhiteVal.empty()){
            dp_white[root] = 1;
            dp_black[root] = 0;
            return;
        }

        pref.push_back(nodeWhiteVal[0] + nodeBlackVal[0]);
        for(int i = 1; i < nodeWhiteVal.size(); i++)
            pref.push_back((1LL * pref[i-1] * (nodeBlackVal[i] + nodeWhiteVal[i])) % mod);

        suf = vector<int> (nodeWhiteVal.size(), 0);
        suf[(int)nodeWhiteVal.size() - 1] = (nodeBlackVal.back() + nodeWhiteVal.back());

        for(int i = (int)nodeWhiteVal.size() - 2; i >= 0; i--)
            suf[i] = (1LL * suf[i+1] * (nodeBlackVal[i] + nodeWhiteVal[i])) % mod;

        dp_white[root] = pref.back();
        dp_black[root] = 0;

        int i = 0;
        for(int child: tree[root]){
            if(child == par)continue;
            int leftWhiteWays = (i == 0) ? 1 : pref[i-1];
            int rightWhiteWays = (i == ((int)nodeWhiteVal.size() - 1)) ? 1 : suf[i+1];
            dp_black[root] = (dp_black[root] +
                    (((1LL * leftWhiteWays * rightWhiteWays) % mod) * dp_black[child]))%mod;
            i++;
        }
    }
}

signed main() {
   fast_io;
   int t = 1; //cin >> t;
   while(t--){
        int n; cin >> n;
        fr(0, n-1){
            int pi; cin >> pi;
            tree[i+1].push_back(pi); tree[pi].push_back(i+1);
        }
        fr(0,n)cin >> blackColor[i];
        solve(0, -1);
        cout << dp_black[0] % mod;
   }
   return 0;
}
```

[Problem - 461B - Codeforces](https://codeforces.com/problemset/problem/461/B)

![Untitled](Apple%20Man%20tree/Untitled%206.png)

<aside>
💡 In Dp we have to consider the subtree more often

</aside>

dp[node][0]= no of ways that subtree have no zero vertex

![Untitled](Apple%20Man%20tree/Untitled%207.png)

![Untitled](Apple%20Man%20tree/Untitled%208.png)

![Untitled](Apple%20Man%20tree/Untitled%209.png)

![Untitled](Apple%20Man%20tree/Untitled%2010.png)

![Untitled](Apple%20Man%20tree/Untitled%2011.png)