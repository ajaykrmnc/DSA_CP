# J - Shushi

Tags: expectation-dp

```cpp
/ one of the big observation is you don’t have to mind in which outcome out of which 1..to ..N is coming instead you can mark you can divide in such a way a group to 0’s 1’s 2’s and 3’s.

Here dp[x][y][z] will represent the state where this state depends upon x no’s of 1’s y no of 2’s, z no of 3’s 

Here p1=(x)/n; corresponding to number of which has exactly no of 1’s shushi’s are in plate
Here p2=(y)/n; corresponding to number of which has exactly no of 2’s shushi’s are in plate
Here p3=(z)/n; similarly

To calculate the no of zeros are (n-(x+y+z)) 
p0 = (n-(x+y+z))/n

So transition between dp state are as follow’s 
dp[i][j][k]= p1* dp[i+1][j][k] + p2* dp[i-1][j+1][k] + p3* dp[i][j-1][k+1] + p0*dp[i][j][k];

since the dp state depends upon own state so we can’t do the same 
(1-p0)dp[i][j][k]= p1* dp[i+1][j][k] + p2* dp[i-1][j+1][k] + p3* dp[i][j-1][k+1] 

or , dp[i][j][k]= (p1* dp[i+1][j][k] + p2* dp[i-1][j+1][k] + p3* dp[i][j-1][k+1])/(1-p0);
```

```cpp
ll dp[301][301][301];
ll solve(int one, int two, int three, int& n){

    if(one < 0 || two < 0 || three < 0)
        return 0;
    if(three == 0 && two == 0 && one == 0)
        return 0;

    if(dp[one][two][three] > 0)
        return dp[one][two][three];

    int remaining = one + two + three;
    ll exp_val = n+one*solve(one-1,two,three,n) +   two*solve(one+1,two-1,three,n) +
                    three*solve(one,two+1,three-1,n);

    return dp[one][two][three] = exp_val/remaining;

}
```

```cpp
const int MX=305;
double dp[MX][MX][MX];

int main() {
  int n;
  scanf("%d",&n);
  vi a(3);
  rep(i,n) {
    int x;
    scanf("%d",&x);
    a[x-1]++;
  }
  double p = 1.0/n;
  for(int k=0;k<n+1;k++)
      for(int j=0;j<n+1;j++)
        for(int i=0;i<n+1;i++) {
             int z = n-i-j-k;
             if (z < 0) break;
             if (z == n) continue;
             double x = 1-z*p;
             if (i) dp[i][j][k] += dp[i-1][j][k]*i*p;
             if (j) dp[i][j][k] += dp[i+1][j-1][k]*j*p;
             if (k) dp[i][j][k] += dp[i][j+1][k-1]*k*p;
             dp[i][j][k] += 1;
             dp[i][j][k] /= x;
  }
  printf("%.10f\n",dp[a[0]][a[1]][a[2]]);
  return 0;
}
```