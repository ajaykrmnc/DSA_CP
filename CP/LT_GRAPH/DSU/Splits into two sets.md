# Splits into two sets

problem link: [Link](https://codeforces.com/problemset/problem/1702/E)

```cpp
struct dsu{
    vector<int>pred,siz;
    dsu(int n){
        pred.resize(n);
        siz.resize(n);
        for(int i=0;i<n;i++){
            siz[i]=1;
            pred[i]=i;
        }
    }
    int get(int a){
        if(pred[a]!=a){
            pred[a]=get(pred[a]);
        }
        return pred[a];
    }
    void merge(int a,int b){
        a=get(a);
        b=get(b);
        if(a!=b){
            if(siz[a]>siz[b])swap(a,b);
            pred[a]=b;
            siz[b]+=siz[a];
        }
    }
};
int32_t main()
{
    speed()
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        map<int,int>mp;
        dsu d(n);
        vector<int>cnt(n);
        for(int i=0;i<n;i++){
            int a,b;
            cin>>a>>b;
            a--;b--;
            cnt[a]++;
            cnt[b]++;
            d.merge(a,b);
        }
        bool ok=true;
        for(int i=0;i<n;i++){
            int sz=d.siz[d.get(i)];
            if(cnt[i]>2 or (sz&1)){
                ok=false;
                break;
            }
        }
        if(ok){
            cout<<"YES"<<nline;
        }else{
            cout<<"NO"<<nline;
        }

    }

    return 0;
}
```

