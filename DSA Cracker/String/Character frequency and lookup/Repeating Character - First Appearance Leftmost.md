# Repeating Character - First Appearance Leftmost

**Problem Statement:**
Given a string, find the index of the first character that appears more than once in the string. Return the leftmost index of the first repeating character. If no character repeats, return -1. For example, in "geeksforgeeks", 'e' appears at indices 1 and 2, and 'g' appears at indices 0 and 10, so the answer is 1 (leftmost repeating character). Use a frequency array to count character occurrences, then traverse the string again to find the first character with frequency > 1. Time complexity is O(n) and space complexity is O(1) for ASCII characters.

```cpp
//User function Template for C++

class Solution
{
    public:
    //Function to find repeated character whose first appearance is leftmost.
    int repeatedCharacter (string s) 
    { 
        //Your code here
        int n=s.length();
        int f[256]={0};
        for(int i=0;i<n;i++)
        {
            f[s[i]]++;
        }
        for(int i=0;i<n;i++)
        {
            if(f[s[i]]>1)
            {
                return i;
            }
        }
        return -1;
    } 
};
```