# SPLAY

**Problem Statement:**
Given an array and multiple range queries, for each query [L, R], find the maximum element in that range. If starting
with D equal to this maximum value, you can traverse the array from the maximum element's position and reach the end of
the range without D becoming less than any array element, output the maximum value. Otherwise, output maximum value + 1.
This problem combines segment trees for range maximum queries with dynamic programming to precompute reachability from
each position. Use DP to calculate the farthest reachable index from each position.

```cpp
#include <bits/stdc++.h>                    #define IOS std::ios::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL);
#define pii pair<int, int>
#define ll long long #define ff first
#define ss second #define rep(i,x,y) for(int i=x; i<y; i++)    using namespace std;
const long long N=500005, INF=2000000000000000000;

int a[N];
pii st[4*N];
void build(int v, int l, int r)
{
  if(l==r)
  {
    st[v]={a[l], -l};
    return;
  }
  int m=(l+r)/2;
  build(v*2, l, m);
  build((v*2)+1, m+1, r);
  st[v]=max(st[v*2], st[(v*2)+1]);
  //cout<<l<<" "<<r<<" "<<t[v].o<<" "<<t[v].c<<" "<<t[v].ans<<"\n";
}
pii query(int v, int tl, int tr, int l, int r)
{
  if(l>r)
    return {-INF, 0};
  if(tl==l&&tr==r)
    return st[v];
  int tm=(tl+tr)/2;
  return max(query((2*v), tl, tm, l, min(tm, r)), query((2*v)+1, tm+1, tr, max(tm+1, l), r));
}

int32_t main()
{
  IOS;
  int t;
  cin>>t;
  while(t--)
  {
    int n, q;
    cin>>n>>q;
    rep(i,0,n)
    cin>>a[i];
    build(1, 0, n-1);
    int dp[n];
    stack <int> s;
    for(int i=n-1;i>=0;i--)
    {
      dp[i]=n;
      while(!s.empty() && a[s.top()]<a[i]-1)
        s.pop();
      if(!s.empty() && a[s.top()]==a[i]-1)
      {
        dp[i]=min(dp[i], dp[s.top()]);
        s.pop();
      }
      if(!s.empty())
        dp[i]=min(dp[i], s.top());
      s.push(i);
    }
    while(q--)
    {
      int l, r;
      cin>>l>>r;
      l--, r--;
      pii p=query(1, 0, n-1, l, r);
      if(dp[-p.ss]<=r)
        cout<<p.ff+1<<"\n";
      else
        cout<<p.ff<<"\n";
    }
  }
}
```

```cpp
#include<bits/stdc++.h>
#define ll long long
#define INF 1e9
using namespace std;

vector<pair<ll, ll>>st(2000005);
vector<ll>a(500005, 0);

pair<ll, ll> merge(pair<ll, ll>&x, pair<ll, ll>&y) {

  ll ind = INF;
  if (x.first == y.first) {
    ind = min(x.second, y.second);
  }
  else {

    if (x.first > y.first) {
      ind = x.second;
    }
    else {
      ind = y.second;
    }
  }

  return {max(x.first, y.first), ind};

}
void buildseg(ll si, ll ss, ll se)
{
  if (ss == se)
  {
    st[si].first = a[ss];
    st[si].second = ss;
    return;
  }
  ll mid = (ss + se) / 2;
  buildseg(2 * si, ss, mid);
  buildseg(2 * si + 1, mid + 1, se);
  st[si] = merge(st[2 * si], st[2 * si + 1]);

}
pair<ll, ll> query(ll si, ll ss, ll se, ll qs, ll qe)
{
  if (ss > qe || qs > se)
  {
    return { -INF, INF};
  }
  if (ss >= qs && qe >= se)
  {
    return {st[si].first, st[si].second};
  }
  ll mid = (ss + se) / 2;
  pair<ll, ll> l = query(2 * si, ss, mid, qs, qe);
  pair<ll, ll> r = query(2 * si + 1, mid + 1, se, qs, qe);
  return merge(l, r);
}

int main()
{
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

  int tc;
  cin >> tc;
  while (tc--) {
    ll n, q;
    cin >> n >> q;
    for (ll i = 1; i <= n; i++)
    {
      cin >> a[i];
    }
    buildseg(1, 1, n);
    vector<ll>lastseen(n + 1, -1);
    map<ll, ll>m;
    for (int i = n; i >= 1; i--) {

      if (m.count(a[i] - 1)) {
        lastseen[i] = m[a[i] - 1];
      }
      m[a[i]] = i;
    }
    vector<ll>nge(n + 1, -1);
    stack<int>pos;
    for (int i = 1; i <= n ; i++) {

      while (!pos.empty() && a[i] >= a[pos.top()])
      {
        nge[pos.top()] = i;
        pos.pop();
      }
      pos.push(i);
    }

    ll dp[n + 1];
    dp[n] = n + 1;
    for (int i = 1; i <= n - 1; i++) {
      dp[i] = n + 1;
    }

    for (int i = n - 1; i >= 1; i--) {

      // S[j]=S[i]-1

      // a[i]-1 is not present

      if (lastseen[i] != -1)
      {
        dp[i] = min(dp[i], dp[lastseen[i]]);
      }
      if (nge[i] != -1)
      {
        dp[i] = min(dp[i], nge[i] - 1);
      }
    }

    ll x, l, r;
    while (q--)
    {
      cin >> l >> r;
      ll mxidn = query(1, 1, n, l, r).second;
      ll mxval = query(1, 1, n, l, r).first;
      if (dp[mxidn] >= r) {
        cout << mxval << '\n';
      }
      else {
        cout << mxval + 1 << '\n';
      }
    }

  }
  return 0;
}
```

The basic approach is that since we need to run 'q' queries and both (r-l) and q lie in range (0 , 5\*10^5) , so to
optimize time, we will construct a segment tree which holds the all the elements of the array and its index as a pair in
its leaf nodes and the maximum of either of its child along with its index in the array as a pair in the internal nodes
.

Here we declare a segment tree as a pair of ll values , for array value and index to be stored.

We declare an array of max size and initialize each element to 0.

This merge function performs two tasks independently.

1. It merges the nodes of the segment tree.
2. It merges the left and right pairs generated in the query function.

This part of the code constructs the leaf nodes of the segment tree and make a call to the merge function passing both
the left and the right child in order to obtain the maximum value of its child and its index.

This query function checks for corner cases and returns the maximum value and its index within the range [qs, qe] from
the segment tree.

This value is of our concern since if dp[max_index] >= r, then it means that we can reach the end by starting with D=
max_val.

Else we would have to start with D = max_val +1.

We declare a map 'm' which stores the index of each element of the array . If they occur multiple times , we only store
the first index.

Using this map, we initialize the values of out vector 'lastseen' which stores the index of value one less than the
current value if the lesser value appears later in the array.

This is made to ensure whether we will be having a decrease in our D value later as the game proceeds and at which
index.

Here we declare a vector 'nge' which holds the index of the next greater element in the array.

Initially we make all the elements of the nge vector as -1, and only update them if for an index, there exists a next
greater element at just the next position.

We have used a stack just to keep track of that indices.

Here we have created our dp array and initialized each of the indices to a max value initially.

dp[i] stores what it the maximum index that can be reachable from the index 'i'.

The basic observation is that , for a certain range [L, R] , the value of the maximum element (maxval) within that range
is the answer if we are able to reach the last index of that range without meeting a condition D<Si .

Else the answer is maxval + 1 Now we only need to check for this condition.

