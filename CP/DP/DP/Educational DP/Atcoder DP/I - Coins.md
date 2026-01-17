# I - Coins

**Problem Statement:**
Given N coins (where N is odd), each with a probability p[i] of landing heads, find the probability that more than half
of the coins land heads when all coins are tossed. Since N is odd, "more than half" means at least (N+1)/2 coins show heads.
This is a probability DP problem where dp[i][j] represents the probability of getting exactly j heads using the first i coins.
The recurrence is: dp[i][j] = dp[i-1][j] * (1-p[i]) + dp[i-1][j-1] * p[i]. Sum up probabilities for all cases where
heads count is at least (N+1)/2.

Tags: probability

```cpp
Let N be a positive odd number.

There are  N coins, numbered  1,2,…,N. For each 
i (1≤i≤N), when Coini is tossed, it comes up heads with probability p 
i and tails with probability  1−pi.

Taro has tossed all the 
N coins. Find the probability of having more heads than tails.
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

int32_t main()
{
    speed()
    int n;
    cin>>n;
    vector<double>v(n);
    mac(i,0,n){
        cin>>v[i];
    }
    double dp[n+5][n+5];
    for(int i=0;i<n+5;i++){
        for(int j=0;j<n+5;j++){
            dp[i][j]=0;
        }
    }
    dp[1][0]=1-v[0];
    dp[1][1]=v[0];
    for(int i=2;i<=n;i++){
        for(int j=0;j<=i;j++){
            // ye match har jaye eske jeet ki count same rahegi
            dp[i][j]+=(dp[i-1][j]*(1-v[i-1]));
            // ye match jeet jaye
            dp[i][j]+=(dp[i-1][j-1]*v[i-1]);
        }
    }
    // for(int i=0;i<=n;i++){
    //     for(int j=0;j<=n;j++){
    //         cout<<dp[i][j]<<' ';
    //     }
    //     cout<<nline;
    // }
    double ans=0;
    for(int i=(n+1)/2;i<=n;i++){
        ans=ans+(double)dp[n][i];
    }
    cout<<setprecision(10)<<ans<<nline;

    return 0;
}
```