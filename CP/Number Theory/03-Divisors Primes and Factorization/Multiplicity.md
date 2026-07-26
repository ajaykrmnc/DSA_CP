# Multiplicity

**Problem Statement:**
Given an array of n positive integers, count the number of subsequences where the i-th element (1-indexed) in the
subsequence is divisible by i. Use dynamic programming where dp[i] represents the number of valid subsequences of length
i. For each element, check all possible lengths it can extend and update the DP accordingly. The key insight is to
iterate through divisors efficiently and maintain DP states for different subsequence lengths.

problem link: https://codeforces.com/problemset/problem/1061/C

```cpp
int32_t main()
{
  speed()
  int n;
  cin>>n;
  vector<int>v(n);
  for(int i=0;i<n;i++){
    cin>>v[i];
  }
  vector<vector<int>>div(n);
  int last=1e6;
  vector<int>dp(last+1,0);
  dp[0]=1;
  for(int i=0;i<n;i++){
    for(int j=1;j<=sqrt(v[i]);j++){
      if(v[i]%j==0){
        div[i].pb(j);
        if(j*j!=v[i]){
          div[i].pb(v[i]/j);
        }
      }
    }
    sort(all(div[i]));
    reverse(all(div[i]));
  }

  for(int i=0;i<n;i++){
    for(auto x: div[i]){
      if(x<=i+1){
        dp[x]+=dp[x-1];
        dp[x]%=mod;
      }
    }
    cout<<nline;
  }
  int ans=0;
  for(int i=1;i<=last;i++){
    if(dp[i]==0){
      break;
    }
    ans+=dp[i];
    ans%=mod;
  }
  cout<<ans<<nline;
  return 0;
}
```

