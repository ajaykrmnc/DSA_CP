# Range Min Max Queries

**Problem Statement:**
Given an array and multiple queries, efficiently answer range minimum and maximum queries along with point updates. For each
query, find both the minimum and maximum elements in a given range [L, R]. The segment tree approach stores pairs (min, max)
for each segment, allowing O(log n) time complexity for both queries and updates. When combining two segments, take the
minimum of minimums and maximum of maximums. This dual-purpose segment tree efficiently handles both min and max operations
simultaneously, making it optimal for problems requiring both statistics.

```cpp
//User function template for C++

// arr : given array arr
// st : segment tree of the given array arr
// n :  size of arr array
// qs and qe : index range to find Min and Max value between these indexes.
// PII :  return pair denoting min,max respectively.
// index : given index to update with new_val

//Function to update a value in input array and segment tree.
PII minimax(int qs,int qe, int ss, int se, int si, PII *st)
{
    //add code here
    if(qe <ss or qs>se) {return {INT_MAX,INT_MIN};}
    if(qs<=ss and qe >= se) {return {st[si].first ,st[si].second};}
    int mid = (ss + se)/2;
    PII val = minimax(qs, qe, ss, mid, 2*si + 1, st);
    PII val1 = minimax(qs, qe, mid + 1, se, 2 *si + 2, st);
    return {min(val.first, val1.first), max(val.second, val1.second)};
}
PII getMinMax(PII *st, int *arr, int n, int qs, int qe){
    minimax(qs,qe,0,n - 1,0, st);
}

//Function to return minimum and maximum of elements in range from index
//qs (quey start) to qe (query end).
void update(int idx, int val,int ss,int se, int si, PII *st)
{
   // add code here
   if(idx < ss or idx > se){
       return;
   }else if(ss == se){
       st[si] = {val,val};
       return;
   }else{
       int mid = (ss + se)/2;
       update(idx, val, ss, mid, 2 * si + 1, st);
       update(idx, val, mid + 1, se, 2 *si + 2 ,st);
       st[si] = {min(st[2 * si + 1].first , st[2 * si + 2].first),max(st[2*si + 1].second, st[2*si + 2].second)};
   }
}
void updateValue(int *arr, PII *st, int n, int index, int new_val){
    arr[index] = new_val;
    update(index, new_val, 0, n-1, 0, st);
}
```