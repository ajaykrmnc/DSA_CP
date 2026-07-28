# Shortest Subarray to be Removed to Make Array Sorted

Remove the shortest contiguous subarray so the remaining array is nondecreasing.

Find the longest sorted prefix and suffix. Then try merging a prefix endpoint with the earliest suffix value that
preserves order.

```cpp
class Solution {
public:
  int findLengthOfShortestSubarray(vector<int>& arr) {
    vector<int> pref, suff;
    int n = arr.size();
    pref.push_back(arr[0]);
    for(int i = 1;i < n; i++) {
      if(arr[i] >= arr[i - 1]) {
        pref.push_back(arr[i]);
      }else break;
    }
    suff.push_back(arr[n - 1]);
    for(int i = n - 2; i >= 0; i--) {
      if(arr[i] <= arr[i + 1]) {
        suff.push_back(arr[i]);
      }else break;
    }
    reverse(suff.begin(), suff.end());
    int suffLen = suff.size(), prefLen = pref.size(), maxLen = suffLen;
    if(suffLen == n) return 0;
    for(int i = 0; i < prefLen; i++) {
      int pos = lower_bound(suff.begin(), suff.end(), pref[i]) - suff.begin();
      maxLen = max(maxLen, suffLen - pos + (i + 1));
    }
    return n - maxLen;
  }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 131 ms
- Memory: 72.7 MB
