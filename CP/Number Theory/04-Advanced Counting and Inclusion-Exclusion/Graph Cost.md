# Graph Cost

problem link: https://codeforces.com/problemset/problem/1731/e

You are given an initially empty undirected graph with 𝑛 nodes, numbered from 1
to 𝑛
(i. e. 𝑛
nodes and 0
edges). You want to add 𝑚
edges to the graph, so the graph won't contain any self-loop or multiple edges.

If an edge connecting two nodes 𝑢 and 𝑣 is added, its weight must be equal to the greatest common divisor of 𝑢
and 𝑣, i. e. gcd(𝑢,𝑣).

In order to add edges to the graph, you can repeat the following process any number of times (possibly zero):

choose an integer 𝑘≥1;
add exactly 𝑘edges to the graph, each having a weight equal to 𝑘+1
. Adding these 𝑘 edges costs 𝑘+1in total.
Note that you can't create self-loops or multiple edges. Also, if you can't add 𝑘
edges of weight 𝑘+1
, you can't choose such 𝑘
.
For example, if you can add 5 more edges to the graph of weight 6
, you may add them, and it will cost 6
for the whole pack of 5
edges. But if you can only add 4
edges of weight 6
to the graph, you can't perform this operation for 𝑘=5
.

Given two integers 𝑛 and 𝑚, find the minimum total cost to form a graph of 𝑛
vertices and exactly 𝑚 edges using the operation above. If such a graph can't be constructed, output −1.

Note that the final graph may consist of several connected components.

```cpp

//****************************Template Ends*******************************//

int main() {
    DIVYA;
    ll t, n, i, j, ans, temp, sum,m;
    string sans;
    t = 1;
    cin >> t;
    while (t--)
    {
        sans = "NO";
        ans = temp = sum = 0;
        cin >> n>>m;
        vll f(n+1,0),g(n+1,0);
        for(i = n;i>0;i--)
        {

            ll cnt = n/i;
            g[i] = (cnt*(cnt-1))/2;
            f[i] = g[i];
            for(j = 2*i;j<=n;j+=i)
            {
                f[i]-=f[j];
            }
        }

        ll taken = 0;
        for(i = n;i>1;i--)
        {
            ll take = min(m - taken,f[i]);
            take = (take/(i-1))*(i-1);
            // cout<<i<<" "<<take<<"\n";
            taken+=take;
            ans+=(i*(take/(i-1)) );
        }
        if(taken != m)ans = -1;
        cout<<ans<<"\n";
    }
    return 0;
}
```

