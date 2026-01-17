# Anagram

**Problem Statement:**
Given two strings, determine if they are anagrams of each other. Two strings are anagrams if they contain the same characters with the same frequency, but possibly in different order. For example, "listen" and "silent" are anagrams. The solution can be implemented by sorting both strings and comparing them, or by counting the frequency of each character in both strings and ensuring they match. The sorting approach has O(n log n) time complexity, while the frequency counting approach has O(n) time complexity with O(1) space for ASCII characters.

```cpp
class Solution
{
    public:
    //Function is to check whether two strings are anagram of each other or not.

    bool isAnagram(string a, string b){
        
        if(a.size()!=b.size()) return false;
        
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        
        if(a!=b) return false;
        return true;
        
    }

};
```