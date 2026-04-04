# Non Repeating Character

Given a string **S** consisting of **lowercase** Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return **'$'.**

**Example 1:**

```cpp
class Solution
{
    public:
    //Function to find the first non-repeating character in a string.
    char nonrepeatingCharacter(string S)
    {
       //Your code here
       int arr[256] = {0};
       int n = S.length();
       for(int i = 0;i < n;i++)
       {
           arr[S[i]]++;
       }
       for(int i = 0;i < n;i++)
       {
           if(arr[S[i]] == 1)
           {
               return S[i];
           }
       }
       return '$';
       
    }

};
```