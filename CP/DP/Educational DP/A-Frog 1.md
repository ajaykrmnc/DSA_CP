# A-Frog 1

**Problem Statement:**
There are N stones numbered 1, 2, ..., N. A frog is initially on stone 1 and wants to reach stone N. From stone i,
the frog can jump to stone i+1 or i+2. The cost of jumping from stone i to stone j is |h[i] - h[j]| where h[i] is the
height of stone i. Find the minimum total cost for the frog to reach stone N. This is a classic dynamic programming
problem where dp[i] represents the minimum cost to reach stone i from stone 1.

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
int dp[N];
int v[N];

int fun(int n)
{
   dp[0]=0;
   dp[1]=abs(v[1]-v[0]);
   if(dp[n]!=-1)
   return dp[n];
   return dp[n]=min(fun(n-1)+abs(v[n]-v[n-1]),fun(n-2)+abs(v[n]-v[n-2]));

}

int32_t main()
{
    speed()
    memset(dp,-1,sizeof(dp));
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>v[i];
    }
    int ans=fun(n-1);
    cout<<ans<<nline;

    return 0;
}
```
