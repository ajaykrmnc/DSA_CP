# Remove Duplicates from Sorted Array II

Remove extra duplicates from a sorted array so each value appears at most twice.

Keep a write index for the valid prefix. A value can be written if fewer than two copies already exist at the end of
that prefix.

```cpp
class Solution {
public:
  int removeDuplicates(vector<int>& nums) {
    int n = nums.size();
    int l = 0, i = 0;
    while(i < n) {
      int curr = nums[i];
      int cnt = 0;
      while(i < n && nums[i] == curr) {
        i++;
        cnt++;
      }
      cnt = min(cnt, 2);
      for(int j = 0; j < cnt; j++) {
        nums[l] = curr;
        l++;
      }
    }
    return l;
  }
};
```
