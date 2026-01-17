# Minimum indexed character

**Problem Statement:**
Given a string str and a pattern patt, find the minimum index of a character in str that also appears in patt. Return the smallest index of any character from patt that appears in str. If no character from patt is found in str, return -1. The approach involves creating an index array to store the minimum index of each character in str, then iterate through patt to find the character with the smallest index. This problem demonstrates efficient character lookup and indexing techniques with O(n+m) time complexity.

```cpp
//User function template for C++

class Solution
{
  public:
    //Function to find the minimum indexed character.
    int minIndexChar(string str, string patt)
    {
        // Your code here
        int idx[26];
        int ans = INT_MAX;
        fill(idx,idx+26,-1);
        int n = str.length();
        int m = patt.length();
        
        // to save minimum index of repeating characters
        for (int i = n-1; i>=0; i--){
            idx[str[i]-'a'] = i;
        }
        for (int i = 0; i<m; i++){
            if (idx[patt[i]-'a'] != -1)
                ans = min(ans,idx[patt[i]-'a']);
        }
        return (ans==INT_MAX)?-1:ans;
    }
};
```