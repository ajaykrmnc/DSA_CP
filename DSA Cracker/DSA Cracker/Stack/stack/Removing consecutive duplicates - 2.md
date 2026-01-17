# Removing consecutive duplicates - 2

**Problem Statement:**
Given a string, remove all consecutive duplicate characters from it. Use a stack-based approach where you compare each
character with the top of the stack. If they are the same, pop the stack (removing the duplicate), otherwise push the
current character. This creates a string where no two consecutive characters are the same. For example, "abbaca" becomes
"ca" after removing consecutive duplicates. This problem demonstrates stack usage for string manipulation and character matching.

```cpp
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution
{
    public:
    string removePair(string s)
    {
        stack<char>stac;
        string final;
        for(int i=0;i<s.size();i++)
        {
            if(!stac.empty())
            {if(stac.top()!=s[i])
            {
                stac.push(s[i]);
            }
            else
            {
                stac.pop();
            }}
            else 
            stac.push(s[i]);
        }
        while(!stac.empty())
        {
            final+=stac.top();
            stac.pop();
        }
        reverse(final.begin(),final.end());
        return final;
       
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin>>t;
    
    while(t--)
    {
        string s;
        cin>>s;
        Solution obj;
        string ans = obj.removePair (s);
        if(ans=="")
            cout<<"Empty String"<<endl;
        else
            cout<<ans<<endl;
    }
    
	return 0;
}  // } Driver Code Ends
```