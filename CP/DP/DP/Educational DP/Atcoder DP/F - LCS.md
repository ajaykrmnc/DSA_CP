# F - LCS

Tags: string

```cpp
#include <bits/stdc++.h>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define nline '\n'

const int mxn=3e3+5;
int dp[mxn][mxn];

string s,str;

int rec(int i,int j){
  //prune
  if(i<0 || j<0)
    return 0;
  if(dp[i][j]!=-1)return dp[i][j];
  int ans=0;
  if(s[i-1]==str[j-1]) {
    ans=1+rec(i-1,j-1);
  } else {
    ans=max(rec(i,j-1),rec(i-1,j));
  }
  return dp[i][j]=ans;
}

int main()
{
    cin>>s>>str;
    int n=s.size();
    int m=str.size();
    memset(dp,-1,sizeof(dp));
    int ans=rec(n,m);
    string final="";
    int i=n,j=m;
    while(i>0&&j>0)
    {
        if(s[i-1]==str[j-1]) { 
            final+=s[i-1];
            i--;
            j--;

        }
        else if(dp[i-1][j] > dp[i][j-1]){
            i--;
        }
        else {
            j--;
        }
    }
    reverse(all(final));
    cout<<final<<nline;

}
```