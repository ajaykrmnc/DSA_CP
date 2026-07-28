# Sort Colors

**LeetCode:** [75. Sort Colors](https://leetcode.com/problems/sort-colors/)  
**Difficulty:** Medium  
**Pattern:** Dutch national flag  
**Tags:** Array, Two Pointers, Sorting

Sort an array containing only 0, 1, and 2 in one pass.

Maintain three regions: placed zeroes, unknown middle, and placed twos. Swap zeroes forward and twos backward while scanning.

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n=nums.size();
        int low=0,high=n-1,i=0;
        while(i<=high){
            if(nums[i]==0 && i>=low){
                swap(nums[i],nums[low++]);
                i--;
            }else if(nums[i]==2){
                swap(nums[i],nums[high--]);
                i--;
            }
            i++;
        }
    }
};
```
