# Euler tour

**Problem Statement:**
This problem involves Euler tour technique on trees, which is a method to flatten a tree into an array while preserving
the tree structure. An Euler tour visits each node exactly twice - once when entering and once when leaving the subtree.
This technique is useful for answering range queries on trees, such as subtree sum queries, LCA queries, and tree path
queries. The flattened array allows us to use segment trees or other range query data structures to efficiently process
tree queries in O(log n) time.

problem link: https://codeforces.com/problemset/problem/1891/F

```cpp
struct data_update{
  int count, node, value;
};
class Solution {
public:
  Solution() {
    vector < vector<int> > graph;
    int n;
    cin >> n;
    vector <data_update>update;
    graph.push_back({});
    int count = 1;
    while(n--){
      int a;
      cin >> a;
      if(a == 2){
        int b, c;
        cin >> b >> c;
        update.push_back({count, b - 1, c});
      }else{
        int b;
        cin >> b;
        int sz = graph.size();
        graph.push_back({b - 1});
        graph[b - 1].push_back(sz);
        count++;
      }
    }
    int timer = 0;
    vector <int> start(graph.size());
    vector <int> end(graph.size());
    vector <int> tour;
    function<void(int, int)>dfs = [&](int at, int prev){
      start[at] = timer++;
      tour.push_back(at);
      for (int n : graph[at]) {
        if (n != prev) { dfs(n, at); }
      }
      end[at] = timer;
    };
    dfs(0, -1);
    int sz = update.size();
    vector <int> ans(graph.size() + 1, 0);
    for(int i = 0; i < sz; i++){
      auto &[count, node, cost] = update[i];
      int lw = lower_bound(tour.begin() + start[node], tour.begin() + end[node], count) - tour.begin();
      pair<int,int> range = {start[node], lw};
      debug(range);
      ans[lw] -= cost;
      ans[start[node]] += cost;
    }
    map<int,int>mp;
    for(int i = 0; i < ans.size(); i++){
      if(i != 0) ans[i] += ans[i - 1];
      if(i != ans.size() - 1){
        mp[tour[i]] = ans[i];
      }
    }
    for(auto &[x, y]: mp){
      cout << y << ' ';
    }
    cout << endl;
  }
};
```

## What kind of problems can be addressed?

Euler tour is useful when a tree problem can be converted into a range problem on an array. After DFS flattening:

- Each node gets an entry time `start[node]`.
- The full subtree of `node` becomes one continuous range:

```cpp
[start[node], end[node])
```

So any data structure that works on array ranges, like prefix sum, Fenwick tree, segment tree, sparse table, or ordered
set, can be used on trees.

Common problem types:

1. **Subtree queries**
   - Find sum/min/max/xor/gcd of values in a subtree.
   - Example: "What is the sum of all nodes inside subtree `u`?"

2. **Subtree updates**
   - Add/set/xor a value to every node in a subtree.
   - Since subtree `u` is `[start[u], end[u])`, this becomes a range update.

3. **Dynamic node value queries**
   - Update value of one node and query subtree aggregate later.
   - Use `start[node]` as the position of that node in the flattened array.

4. **Ancestor/subtree checks**
   - Check whether `u` is ancestor of `v`:

```cpp
start[u] <= start[v] && start[v] < end[u]
```

5. **Offline tree updates**
   - Apply operations that affect all currently existing nodes in a subtree.
   - Process queries using Euler order plus prefix difference/range updates.

6. **Path queries with extra technique**
   - Euler tour alone is best for subtree ranges.
   - For path queries like `u` to `v`, combine it with LCA, Heavy-Light Decomposition, or prefix-from-root values.

Typical examples:

- Subtree sum queries.
- Count colors/frequencies in a subtree.
- Add value to every node in a subtree.
- Check if one node lies inside another node's subtree.
- Answer offline queries on dynamically built trees.
- Compute entry/exit times for ancestor logic.

---
