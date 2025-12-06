# Counting Graph

[Problem - G - Codeforces](https://codeforces.com/contest/1857/problem/G)

Given a tree consisting of 𝑛 vertices. A tree is a connected undirected graph without cycles. Each edge of the tree has its weight, 𝑤𝑖.

Your task is to count the number of different graphs that satisfy all four conditions:

1. The graph does not have self-loops and multiple edges.
2. The weights on the edges of the graph are integers and do not exceed .
    
    𝑆_i
    
3. The graph has **exactly one** [minimum spanning tree](http://tiny.cc/30g9vz).
4. The minimum spanning tree of the graph is the given tree.

Two graphs are considered different if their sets of edges are different, taking into account the weights of the edges.

The answer can be large, output it modulo 998244353998244353.

```cpp

const int mod = 998244353;
int binexp(int n,int m){
    int st = 1;
    while(m >0){
        if((m & 1) != 0){
            m-=1;
            st*=n;
        }
        n*=n;
        m = m >> 1;
        st%=mod;
        n%=mod;
    }
    return st;
}
class solve{
    public:
    class dsu{
        public: 
        vector<int>siz,par,val;
        dsu(int n){
            siz.resize(n);
            par.resize(n);
            val.resize(n);
            for(int i = 0; i < n;i++){
                siz[i] = 1;
                par[i] = i;
                val[i] = 1;
            }
        }
        int get(int a){
            if(a == par[a])return a;
            return par[a] = get(par[a]);
        }
        void merge(int a,int b,int w){
            a = get(a);
            b = get(b);
            if(siz[a] > siz[b])
                swap(a,b);
            par[a] = b;
            int ans = (val[a]*val[b] % mod) * binexp(w,(siz[a]*siz[b] - 1)) % mod;
            siz[b] += siz[a];
            val[b] = ans;
        }

    };
    solve(){
        int n,s;
        cin>>n>>s;
        vector<vector<int>>edges(n - 1);
        for(int i = 0; i < n - 1; i++){
            vector<int>edge(3);
            int a,b,w;
            cin>>a>>b>>w;
            a--;b--;
            edge = {w,a,b};
            edges[i] = edge;
        }
        sort(edges.begin(),edges.end());
        debug(edges);
        dsu d(n);
        int ans = 0;
        for(int i = 0; i < n - 1; i++){
            auto &edge = edges[i];
            d.merge(edge[1],edge[2],s - edge[0] + 1);
        }
        cout << d.val[d.get(0)] << endl;
    }
};

int32_t main() {
    int t=1;
    cin>>t;
    while(t--){
        solve obj;
    }
    return 0;
}
```