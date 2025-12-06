# Round Dance

```cpp
struct dsu{
    vector<int>count,pred;
    dsu(int n){
        count.resize(n,1);
        pred.resize(n);
        for(int i=0;i<n;i++){
            pred[i]=i;
        }
    }
    int get(int p){
        if(pred[p]!=p){
            pred[p]=get(pred[p]);
        }
        return pred[p];
    }
    bool check(int a,int b){
        return get(a)==get(b);
    }
    void merge(int a,int b){  
        a=get(a);
        b=get(b);
        if(a==b)return;
        if(count[a]>count[b]){   // b for bada
            swap(a,b);
        }
        pred[a]=pred[b];
        count[b]+=count[a];
    }
};
int32_t main()
{
    speed()
    int t=1;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        dsu d(n);
        vector<int>v(n);
        for(auto &x: v){
            cin>>x;
            x--;
        }
        map<int,set<int>>mp;
        for(int i=0;i<n;i++){
            d.merge(i,v[i]);
            int mini=min(i,v[i]);
            int maxi=max(i,v[i]);
            mp[mini].insert(maxi);
            pair<int,int>pii={mini,maxi};
        }
        set<int>st;
        // debug(mp);
        map<int,int>mp2;
        for(int i=0;i<n;i++){
            st.insert(d.get(i));
            mp2[d.get(i)]+=mp[i].size();
        }
        debug(st);
        debug(mp2);
        int count=0;
        for(auto x: st){
            if(mp2[x]==d.count[x]){
                count++;
            }
        }
        if(count==st.size()){
            cout<<count<<' '<<st.size()<<nline;
        }else{
            cout<<1+count<<' '<<st.size()<<nline;
        }

    }
    return 0;
}
```