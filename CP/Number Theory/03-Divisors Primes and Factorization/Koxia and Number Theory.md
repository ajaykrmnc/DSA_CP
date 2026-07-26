# Koxia and Number Theory

problem link: [Link](https://codeforces.com/problemset/problem/1770/C)

Joi has an array 𝑎 of 𝑛 positive integers. Koxia wants you to determine whether there exists a positive integer 𝑥>0
such that gcd(𝑎𝑖+𝑥,𝑎𝑗+𝑥)=1 for all 1≤𝑖<𝑗≤𝑛

```cpp
bool solve(){
  int n;
  cin>>n;
  vector<int>v(n),primes;
  for(int i=0;i<n;i++)cin>>v[i];
  sort(all(v));
  mac(i,1,n){
    if(v[i]==v[i-1])return false;
  }
  for(int i=2;i<60;i++){
    for(int j=2;j<=i;j++){
      if(j==i){
        primes.push_back(i);
      }
      if(i%j==0){
        break;
      }
    }
  }
  for(int j=0;j<primes.size();++j){
    int prime=primes[j];
    vector<int>modulo(prime);
    for(int i=0;i<n;i++){
      modulo[v[i]%prime]++;
    }
    if(*min_element(modulo.begin(),modulo.end())>=2){
      return false;
    }
  }
  return true;
}

int32_t main()
{
  speed()
  int t;
  cin>>t;
  while(t--){
    if(solve()){
      cout<<"YES"<<nline;
    }else
    cout<<"NO"<<endl;
  }

  return 0;
}
```

## Approach

If two numbers are equal, then after adding the same `x` they also stay equal, so their gcd cannot become `1` unless the
value itself is `1`; this case is impossible here, so duplicates directly give `NO`.

For any prime `p`, if every residue class modulo `p` already contains at least two numbers, then no matter what `x` we
choose, one pair will become divisible by `p` together. That pair will have gcd greater than `1`, so answer is `NO`.

So we check all small primes below `60`, count `a[i] % p`, and if every bucket has count at least `2`, we fail. If no
prime creates this obstruction, answer is `YES`.
