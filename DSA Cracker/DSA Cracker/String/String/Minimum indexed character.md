# Minimum indexed character

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