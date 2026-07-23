# Find Second Maximum

**Problem Statement:**
Given an array and multiple queries, handle two types of operations: 1) Update an element at a given index, 2) Find the
count of occurrences of the second maximum element in a given range [L, R]. For each range query, you need to identify
the second largest value and return how many times it appears in that range. This problem requires a segment tree that
maintains both the maximum and second maximum values along with their counts for efficient range queries and updates.
Each segment tree node stores the maximum, second maximum, and their respective counts to enable efficient merging of
child node information.

```cpp
struct infor{
  int max1, max2, cnt1, cnt2;
};

class SegmentTree
{
public:
  //Function to find max of given range.
  infor maxi(infor pii1, infor pii2){
    map<int, int, greater<int>>temp;
    temp[pii1.max1] += pii1.cnt1;
    temp[pii1.max2] += pii1.cnt2;
    temp[pii2.max1] += pii2.cnt1;
    temp[pii2.max2] += pii2.cnt2;
    if(temp.size() == 1){
      return {temp.begin()->first, -1, temp.begin()->second, 0};
    }else{
      auto &[num, cnt1] = *temp.begin();
      temp.erase(num);
      auto &[num2, cnt2] = *temp.begin();
      return {num,num2, cnt1, cnt2};
    }
  }
  int n, *arr;
  infor *st;
  infor maxUtil(int l, int r, int ss, int se, int si){
    if(r<ss or l>se){return {-1, -1};}
    if(l<=ss and r>=se){return st[si];}
    int mid= (ss+se)/2;
    return maxi(maxUtil(l,r, ss, mid, 2 * si + 1), maxUtil(l,r, mid + 1, se, 2 * si + 2));
  }
  infor findRangemax(int l, int r)
  {
    // code here
    return maxUtil(l, r, 0, n - 1, 0);
  }
  void update(int idx,int val,int ss,int se,int si){
    if(idx<ss or idx>se){
      return;
    }else if(ss == se){
      st[si]={val, -1, 1, 0};
      return;
    }
    int mid = (ss+se)/2;
    update(idx,val,ss,mid,2*si+1);
    update(idx,val,mid+1,se,2*si+2);
    st[si] = maxi(st[si * 2 + 1], st[si * 2 + 2]);
  }
  //Function to update a value in input array and segment tree.
  void updateValue(int index, int new_val)
  {
    // code here
    arr[index]=new_val;
    update(index,new_val, 0, n-1, 0);
  }
  SegmentTree(int n, int *inputArr){
    this->n = n;
    arr = new int[n]();
    st  = new infor[4 * n]();
    for(int i = 0; i < n; i++){updateValue(i, inputArr[i]);}
  }
};
class Solution {
public:
  Solution() {
    int n, q;
    cin >> n >> q;
    int arr[n];
    for(auto it = arr; it != arr + n; it++){
      cin >> *it;
    }
    SegmentTree sgtree(n, arr);
    for(int i = 0; i < q; i++){
      int a, b, c;
      cin >> a >> b >> c;
      if(a == 1){
        sgtree.updateValue(b - 1, c);

      }else{
        infor response = sgtree.findRangemax(b - 1, c - 1);
        cout << response.cnt2 << endl;
      }
    }

  }
};

int32_t main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL),cout.tie(NULL);
  int t = 1;
  // cin >> t;
  while (t--) {
    Solution obj;
  }
  return 0;
}
```
