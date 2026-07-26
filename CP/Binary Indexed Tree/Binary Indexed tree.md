# Binary Indexed tree

**Problem Statement:**
Binary Indexed Tree (BIT) or Fenwick Tree is a data structure that efficiently supports range sum queries and point
updates in O(log n) time. Given an array, you need to handle two types of operations: update a single element and query
the sum of elements in a range [l, r]. BIT uses the binary representation of indices to store partial sums in a
tree-like structure.
The key insight is that each index in BIT is responsible for a range of elements determined by the least significant
bit. This allows both updates and queries to be performed by traversing at most log n nodes in the tree.

[Problem - E2 - Codeforces](https://codeforces.com/contest/1579/problem/E2)

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vb = vector<bool>;
using vvb = vector<vb>;
using vi = vector<int>;
using vvi = vector<vi>;
using vl = vector<ll>;
using vvl = vector<vl>;
using vc = vector<char>;
using vvc = vector<vc>;
using vs = vector<string>;
const ll mod = 1e9 + 7,inf = 1e18;
struct BIT
{
  vl bit;
  int n;
  BIT(int N)
  {
    n = N;
    bit.assign(n + 1,1ll * 0);
  }
  void update(int i,ll inc)
  {
    for (;i<=n;i += i & -i)bit[i] += inc;
  }
  ll query(int i)
  {
    ll ret = 0;
    for (;i>0;i -= i & -i)ret += bit[i];
    return ret;
  }
  ll query(int l,int r)
  {
    return query(r) - query(l - 1);
  }
};
int main()
{
  setIO();
  int t;
  cin>>t;

  while (t--){
    int n;
    cin>>n;
    map<int,int>freq;
    map<int,int>positions;
    vi a(n);

    for (int i = 0;i<n;i++){
      cin>>a[i];
      freq[a[i]]++;
    }

    int pos = 1;
    for (auto it:freq)
    positions[it.first] = pos++;

    for (int i = 0;i<n;i++)
      a[i] = positions[a[i]];

    BIT ds(n);

    //deque<int>q;
    //q.push_back(a[0]);

    ds.update(a[0],1);
    ll ans = 0;//total number of inversions

    for (int i = 1;i<n;i++){
      ll opt1 = ds.query(1,a[i] - 1);//the cost for pushing a[i] to the beginning
      ll opt2 = ds.query(a[i] + 1,n);//the cost for pushing a[i] to the back
      ans += min(opt1,opt2);

      //if (opt1 < opt2)q.push_front(a[i]);
      //else q.push_back(a[i]);

      ds.update(a[i],1);
    }

    cout<<ans<<endl;
  }
  return 0;
}
```

# Introduction

Coordinate compression is a technique to map a large set of points to a smaller range by removing gaps and/or redundant
information. By compressing the points to a smaller range, we can save considerable time and memory.

Most of you would have unknowingly applied 1D coordinate compression but it’s 2D coordinate compression that is
extremely powerful. This blog post explains both cases.

# Coordinate Compression In 1D

The simplest example of coordinate compression is sorting a 1D array.
Suppose we have an array A[] of size N. After sorting, the element A[i] is mapped to index i. This way, elements that
were in an arbitrary range are now mapped to the range [0, N-1] and yet their relative ordering is preserved.
Sounds trivial? This proves to be very useful. Let’s check out an example.

1D Coordinate Compression: Mapping an array of N numbers to the range [0, N-1].

![](Binary%20Indexed%20tree/1nAucVgQ-lckNQZHDIG1Gnw.png)

```cpp
class BinaryIndexedTree{
public:
  int *arr, n;
  BinaryIndexedTree(int n) : n(n){
    arr = new int[n + 1]();
  }
  void update(int pos){
    for(; pos <= n; pos += (pos & (-pos))){
      arr[pos] += 1;
    }
  }
  int rangeSum(int r){
    int sum = 0;
    for(; r > 0; r -= (r & (-r))){
      sum += arr[r];
    }
    return sum;
  }
  int query(int l, int r){
    return rangeSum(r) - rangeSum(l);
  }
};

class Solution {
public:
  vector<int> resultArray(vector<int>& nums) {
    map<int,int>mp;
    vector<int>sorted = nums;
    sort(sorted.begin(), sorted.end());
    int n = nums.size();
    int idx = 1;
    for(int i = 0; i < n; i++){
      if(mp.find(sorted[i]) == mp.end()){
        mp[sorted[i]] = idx++;
      }
    }
    vector<int>fi,se;
    int m = mp.size();
    BinaryIndexedTree forFirst(m), forSecond(m);
    forFirst.update(mp[nums[0]]);
    forSecond.update(mp[nums[1]]);
    fi.push_back(nums[0]);
    se.push_back(nums[1]);
    for(int i = 2; i < n; i++){
      int cnt1 = forFirst.query(mp[nums[i]], m);
      int cnt2 = forSecond.query(mp[nums[i]], m);
      if(cnt2 > cnt1 or (cnt1 == cnt2 and fi.size() > se.size())){
        forSecond.update(mp[nums[i]]);
        se.push_back(nums[i]);
      }else{
        forFirst.update(mp[nums[i]]);
        fi.push_back(nums[i]);
      }
    }
    cout << endl;
    vector<int>ans;
    for(auto &x: fi){ans.push_back(x);}
    for(auto &x: se){ans.push_back(x);}
    return ans;
  }
};
```

[problem](https://leetcode.com/contest/weekly-contest-387/problems/distribute-elements-into-two-arrays-ii/)

