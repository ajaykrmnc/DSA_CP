# Repeating Character - First Appearance Leftmost

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