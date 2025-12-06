# Mex tree

```cpp
const int N=2e5+5;
vector<int>v[N];
int siz[N];
int lvl[N];
int forefather[N];

int tim=0,st[N],et[N];
void dfs(int z,int p=-1,int ff=0){
    if(p==-1) lvl[z]=0;
    else lvl[z]=lvl[p]+1;

    if(lvl[z]==1)ff=z;
    forefather[z]=ff;

    st[z]=tim++;
    siz[z]=1;
    for(int x: v[z]){
        if(x==p) continue;
        dfs(x,z,ff);
        siz[z]+=siz[x];
    }
    et[z]=tim;
}

// x is ancestor of y
bool ancestor(int x,int y){
    if(st[y]>st[x] && et[y]<= et[x]){
        return true;
    }
    return false;
}

int calc(int x,int y){
    if(y==0) swap(x,y);
    if(x==0){
        return siz[y]*(siz[0]-siz[forefather[y]]);
    }
    return siz[x]*siz[y];
}

void solve(){
    tim=0;
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        v[i].clear();
        siz[i]=0;
        lvl[i]=0;
        forefather[i]=0;
    }
    for(int i=1;i<n;i++){
        int x,y;
        cin>>x>>y;
        v[x].pb(y);
        v[y].pb(x);
    }
    dfs(0);
    int paths=n*(n-1)/2;
    int donthavezero=0;
    for(int i=1;i<n;i++){
        if(lvl[i]!=1)continue;
        donthavezero+=(siz[i]*(siz[i]-1))/2;
    }
    cout<<donthavezero<<' ';
    paths-=donthavezero;
    int a=0,b=0;

    for(int i=1;i<n;i++){
        if(paths==0){
            cout<<0<<' ';
            continue;
        }
        if(a==0) swap(a,b);
        if(ancestor(i,a)||ancestor(i,b)){
            cout<<0<<" ";
            continue;
        }
        if(ancestor(a,i)){
            a=i;
            int wont_work=calc(a,b);
            cout<<paths-wont_work<<' ';
            paths=wont_work;
        }else if(ancestor(b,i)){
            if(forefather[i]==forefather[a]){
                cout<<paths<<" ";
                paths=0;
                continue;
            }
            b=i;
            int wont_work=calc(a,b);
            cout<<paths-wont_work<<' ';
            paths=wont_work;
        }else{
            cout<<paths<<' ';
            paths=0;
        }
    }
    cout<<paths;
    cout<<"\n";;
}

int32_t main()
{
    speed()
    int t;
    cin>>t;
    while(t--){
        solve();
    }

    return 0;
}
```

[Problem - D - Codeforces](https://codeforces.com/contest/1527/problem/D)