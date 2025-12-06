# A-Frog 1

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
