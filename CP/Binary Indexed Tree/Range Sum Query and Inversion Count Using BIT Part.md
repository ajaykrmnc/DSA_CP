# Range Sum Query and Inversion Count Using BIT | Part 2

**Problem Statement:**
This problem demonstrates using Binary Indexed Tree (BIT) to efficiently count inversions in an array. An inversion is a
pair of indices (i,j) where i < j but arr[i] > arr[j]. The naive approach takes O(n²) time, but using BIT with
coordinate compression reduces it to O(n log n). Process elements from right to left, for each element query the count
of smaller elements seen so far, then update the BIT. Coordinate compression maps array values to indices 1 to n for BIT
operations.

```cpp
#include<bits/stdc++.h>
using namespace std;

#define int long long

const int N = 1e6 + 10;

int n, a[N], bit[N];

void upd(int x, int v){
  for(int i = x; i <= n; i += i & -i)
    bit[i] += v;
}

int query(int x){
  int sum = 0;
  for(int i = x; i > 0; i -= i & -i)
    sum += bit[i];
  return sum;
}

int inv_cnt(){
  int cnt = 0;
  for(int i = n; i >= 1; --i){
    cnt += query(a[i] - 1);
    upd(a[i], 1);
  }
  return cnt;
}

signed main(){
  cin >> n;
  for(int i = 1; i <= n; ++i)
    cin >> a[i];
  cout << inv_cnt() << endl;
  return 0;
}
```

