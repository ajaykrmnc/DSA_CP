# Magic Triples

**Problem Statement:**
Given an array of integers, count the number of triples (i, j, k) where i < j < k and `arr[i] * arr[j] = arr[k]`. These
are called "magic triples" because the product of the first two elements equals the third element.

The challenge is to efficiently count such triples without checking all possible combinations. This can be solved using
frequency maps and mathematical properties. For each pair (i, j), check if their product exists in the array at a
position k > j. Use data structures like maps or sets to optimize the search and counting process.

problem link: https://codeforces.com/contest/1822/problem/G1

```cpp
int32_t main()
{
  speed()
  int t;
  cin>>t;
  vector<int>count(1e6+10,0);
  while(t--){
    int n;
    cin>>n;
    vector<int>v(n);
    for(auto &x: v){
      cin>>x;
    }
    map<int,int>mp;
    for(int i=0;i<n;i++){
      mp[v[i]]++;
      count[v[i]]++;
    }
    int ans=0;
    for(auto [x,cnt]: mp){
      if(cnt>2){
        int res=(cnt*(cnt-1)*(cnt-2));
        ans+=res;
      }
    }
    for(int i=0;i<n;i++){
      int res=v[i];
      for(int j=2;res*j*j<(1e6+10);j++){
        int cnt=1;
        cnt*=count[v[i]*j];
        cnt*=count[v[i]*j*j];
        pair<int,int>pii={v[i],j};
        if(cnt!=0){
          debug(pii);
          debug(cnt);
        }
        ans+=cnt;
      }
    }
    for(int i=0;i<n;i++){
      // mp[v[i]]++;
      count[v[i]]--;
    }
    cout<<ans<<nline;
  }

  return 0;
}
```

