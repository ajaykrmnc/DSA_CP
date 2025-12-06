# H - Grid I

Tags: grid

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
const int mod=1e9+7;
int32_t main()
{
    speed()
    int t;
    t=1;
    while(t--){
        int n;
        cin>>n;
        int m;
        cin>>m;
        int dp[n][m];
        memset(dp,0,sizeof dp);
        vector<string>v(n);
        for(int i=0;i<n;i++){
            cin>>v[i];
        }
        if(v[0][0]=='#'){
            dp[0][0]=0;
        }else {
            dp[0][0]=1;
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(v[i][j]=='#'){
                    continue;
                }
                if(i>0)
                if(v[i-1][j]=='.'){
                    dp[i][j]+=dp[i-1][j];
                }
                if(j>0)
                if(v[i][j-1]=='.'){
                    dp[i][j]+=dp[i][j-1];
                }
                dp[i][j]%=mod;
            }
        }
        cout<<dp[n-1][m-1]<<nline;
    }

    return 0;
}
```