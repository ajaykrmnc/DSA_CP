# Binary String
**Problem Statement:**
Given a binary string S, count the number of substrings that start and end with 1. For example, if the input string is
"00100101", then there are three substrings "1001", "100101" and "101". The key insight is that if there are n occurrences
of '1' in the string, then the number of valid substrings is nC2 = n*(n-1)/2. This is because any two '1's can form
a valid substring. Simply count all '1's in the string and apply the combination formula. Time complexity is O(n) and
space complexity is O(1).

Given a binary string S. The task is to count the number of substrings that start and end with 1. For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.

```cpp
class Solution
{
    public:
    //Function to count the number of substrings that start and end with 1.
    long binarySubstring(int n, string a){

        // Your code here
        long ans = 0;

        for(int i=0;i<n;i++){
            if(a[i]=='1')
            ans++;
        }

        return (ans*(ans-1))/2;
    }

};
```