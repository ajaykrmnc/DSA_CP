# Naive Pattern Search

```cpp
class Solution
{
    public:
    //Function to check if the given pattern exists in the given string or not.
    bool search(string pat, string txt) 
    { 
        
        // Your code here
        int n = txt.size();
        int m = pat.size();
        for(int i=0; i<n-m+1;){
            int j=0;
            while(txt[i] == pat[j] && j<m){
                j++;
                i++;
            }
            if(j==m){
                return true;
            }
            if(j==0){
                i++;
            }
        }
        return false;
    }
};
```