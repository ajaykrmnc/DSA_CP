# B- frog2

**Problem Statement:**
Similar to Frog 1, but now the frog can jump to any stone from i+1 to i+k (instead of just i+1 or i+2). Given N stones
and a parameter k, find the minimum cost for the frog to reach stone N from stone 1. The cost of jumping from stone i to
stone j is |h[i] - h[j]|. Use dynamic programming where dp[i] represents minimum cost to reach stone i, considering all
possible jumps from previous k stones. This extends the basic DP concept to handle variable jump distances.

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
const int N =1000000;
int maxi=1000005;
int dp[N];
int v[N];

int fun(int n,int k) {
      if(n==0)
		      return 0;
	    if(dp[n]!=-1)
	       return dp[n];
      int cost=maxi;
      for(int j=1;j<=k;j++)
      {
           if(n-j>=0)
           cost=min(cost,fun(n-j,k)+abs(v[n]-v[n-j]));
           
       }
       return dp[n]=cost;
}

int32_t main()
{
    speed()
    memset(dp,-1,sizeof(dp));
    int n,k;
    cin>>n>>k;
    for(int i=0;i<n;i++){
        cin>>v[i];
    }
    int ans=fun(n-1,k);
    cout<<ans<<nline;

    return 0;
}
```