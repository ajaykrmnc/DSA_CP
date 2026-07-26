# two array with binary search

**Problem Statement:**

```cpp
int32_t main()
{
  speed()
  int t;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    vector<pair<int,int>>pii(n);
    for(int i=0;i<n;i++){
      int a,b;
      cin>>a>>b;
      pii[i]={a,b};
    }
    sort(all(pii));
    vector<int>suf(n+1);
    suf[n]=0;
    for(int i=n-1;i>=0;i--){
      suf[i]=max(pii[i].second,suf[i+1]);
    }
    set<int>st;
    int ans=inf;
    for(int i=0;i<n;i++){
      if(i==n-1){
        int res=inf;
        auto it=st.upper_bound(pii[i].first);
        if(it!=st.end()){
          res=min(abs(*it-pii[i].first),res);
        }
        {
          if(it!=st.begin()){
            it--;
            res=min(abs(*it-pii[i].first),res);
          }
        }
        ans=min(ans,res);
        continue;
      }
      int res=abs(suf[i+1]-pii[i].first);
      if(suf[i+1]>=pii[i].first){
        res=res;
      }else{
        auto it=st.upper_bound(pii[i].first);
        if(it!=st.end()){
          res=min(abs(*it-pii[i].first),res);
        }
        {
          if(it!=st.begin()){
            it--;
            if(*it>=suf[i+1]){
              res=min(abs(*it-pii[i].first),res);
            }
          }
        }
      }
      st.insert(pii[i].second);
      ans=min(ans,res);
    }
    cout<<ans<<nline;

  }

  return 0;
}
```
