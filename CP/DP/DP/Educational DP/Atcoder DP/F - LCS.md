# F - LCS

**Problem Statement:**
Given two strings s and t, find the Longest Common Subsequence (LCS). A subsequence is a sequence that can be derived from
another sequence by deleting some or no elements without changing the order of remaining elements. The LCS problem asks
for the longest subsequence that appears in both strings. Use dynamic programming where dp[i][j] represents the length
of LCS of first i characters of s and first j characters of t. Also track the actual LCS string using backtracking.

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