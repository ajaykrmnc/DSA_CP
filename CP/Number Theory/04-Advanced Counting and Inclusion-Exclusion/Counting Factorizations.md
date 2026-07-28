# Counting Factorizations

**Problem Statement:**
Given 2n integers, you need to pair them such that each pair forms a factorization a\*b where a is prime and b is
composite.
Count the number of ways to create n such pairs. This problem involves number theory concepts like prime factorization
and combinatorics. You need to identify which numbers are prime and which are composite, then use dynamic programming
or combinatorial counting to determine valid pairings. The solution involves sieve for prime detection, factorial
calculations for permutations, and careful handling of constraints to avoid invalid pairings.

problem link: https://codeforces.com/problemset/problem/1794/D

```cpp
const int mod=998244353;
const int maxn=2025;
int fact[maxn];
int inv_fact[maxn];
int binexp(int n,int p){
  int ans=1;
  while(p>0){
    if(p&1){
      ans=ans*n%mod;
    }
    n*=n;
    n%=mod;
    p>>=1;
  }
  return ans;
}

int spf[5000001];
int pre[5000001];
int sizee=1e6+10;
vector<int>primes;
void sieve(){
  for(int i=0;i<=sizee;i++)
    spf[i]=i;

  for(int i=2;i*i<=sizee;i++){
    if(spf[i]==i){
      for(int j=i*i;j<=sizee;j+=i){
        if(spf[j]==j)
          spf[j]=i;
      }
    }
  }
  for(int i=2;i<=sizee;i++){
    if(spf[i]==i){
      primes.pb(i);
    }
  }
}
void solve(){
  fact[0]=1;
  fact[1]=1;
  for(int i=1;i<maxn;i++){
    fact[i]=fact[i-1] * i % mod;
  }
  inv_fact[0]=1;
  inv_fact[1]=1;
  for(int i=1;i<maxn;i++){
    int res=binexp(fact[i],mod-2);
    inv_fact[i] = res;
  }
}
int32_t main()
{
  speed()
  sieve();
  solve();
  int n;
  cin>>n;
  vector <int> v (2*n);
  for(int i=0;i<2*n;i++){
    cin >> v[i];
  }
  map <int,int> mprime;
  map <int,int> nprime;
  int p = 0,np = 0;
  for(int i = 0;i < 2 * n; i++){
    if(binary_search(all(primes),v[i])){
      mprime[v[i]]++;
      p++;
    }else{
      nprime[v[i]]++;
      np++;
    }
  }
  int ans=fact[n];
  if(p<n){
    cout<<0<<nline;
    return 0;
  }
  for(auto [x,y]: nprime){
    ans*=(inv_fact[y]);
    ans%=mod;
  }
  // for(auto [x,y]: nprime){
  //     cout<<nline;
  //     cout<<x<<' ';
  //     cout<<nline;
  // }
  int m=mprime.size()+1;
  int need=n-np;
  vector<vector<int>>dp(m,vector<int>(need+1,0));
  // initiallisation
  dp[0][0]=1;
  int it=0;
  for(auto [x,y]: mprime){
    // yaha se dp lagna start ho raha hai
    // we have to chose the n primes out of total primes
    // such that the chosen primes contribute the (its_cnt-1) to the inverse fact calculation
    // if we start dp for each prime
    // we can do the knapsack such that is included or not // if it is included then it is // from
    dp[i][0]....dp[i][need] me inv_fact[its_cnt-1] se multiply karke inko update kar denge
    // else exclude rakhnge  for(int j=0;j<need+1;j++){
    for(int i=0;i<2;i++){
      if(j+y-i<=need){
        dp[it+1][j+y-i]+=dp[it][j]*inv_fact[y-i]%mod;
        dp[it+1][j+y-i]%=mod;
      }
    }
  }
  it++;
}
cout<<ans*dp[m-1][need]%mod;


return 0;
}
```

