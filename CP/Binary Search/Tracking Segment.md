# Tracking Segment

**Problem Statement:**
You have an array of n zeros and m segments. You also have q queries that set array elements to 1. Find the
minimum number of queries needed to make at least one segment "good". A segment [l, r] is good if more than
half of its elements are 1s. Use binary search on the answer - for each potential number of queries, check if
any segment becomes good after applying that many queries. The solution involves prefix sums to efficiently
count 1s in segments and binary search to find the minimum number of queries required.

problem link: https://codeforces.com/contest/1843/problem/E

```cpp
#
bool pred(int mid,int n,vector<int>&query,vector<pair<int,int>>&pii){
  vector<int>pre(n,0);
  int sum=0;
  vector<int>v(n);
  for(int i=0;i<mid;++i){
    v[query[i]]=1;
  }
  for(int i=0;i<n;i++){
    if(v[i]==1){
      sum++;
    }
    pre[i]=sum;
  }
  debug(v);
  debug(pre);
  int flag=0;
  for(int i=0;i<pii.size();i++){
    int len=pii[i].second-pii[i].first+1;
    int res=0;
    if(pii[i].first==0){
      res=pre[pii[i].second];
    }else{
      res=pre[pii[i].second]-pre[pii[i].first-1];
    }
    if(res>=(len)/2+1){
      flag=1;
      debug(res);
      debug(mid);
      debug(len);
    }
  }
  return flag;
}

int32_t main() {
  fastio();
  int t=1;
  cin>>t;
  while(t--){
    int n,m;
    cin>>n>>m;
    vector<pair<int,int>>pii;
    for(int i=0;i<m;i++){
      int a,b;
      cin>>a>>b;
      a--;b--;
      pii.pb({a,b});
    }
    int q;
    cin>>q;
    vector<int>query(q);
    for(int i=0;i<q;i++){
      int a;
      cin>>a;
      a--;
      query[i]=a;
    }
    debug(query);
    debug(pii);
    int lo=0;
    int hi=q;
    int ans=-1;
    while(lo<=hi){
      int mid=lo+(hi-lo)/2;
      if(!pred(mid,n,query,pii)){
        lo=mid+1;
      }else{
        ans=mid;
        hi=mid-1;
      }
    }
    cout<<ans<<nline;
  }
  return 0;

}
```

