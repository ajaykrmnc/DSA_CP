# Removing consecutive duplicates

**Problem Statement:**
Given a string, remove all consecutive duplicate characters from it. Use a stack-based approach where you compare each character with the top of the stack. If the current character is different from the top of the stack, push it onto the stack. If they are the same, skip the current character (don't push). Finally, pop all characters from the stack to form the result string. This approach ensures that no two consecutive characters in the final string are the same, effectively removing consecutive duplicates.

```cpp
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution
{
    public:
    string removeConsecutiveDuplicates(string s)
    {
        stack<char>stac;
        for(int i=0;i<s.size();i++)
        {
            if(!stac.empty())
            {
            
                if(s[i]!=stac.top())
                {
                    stac.push(s[i]);
    
                    
                }
            }
                else 
                {
                    stac.push(s[i]);
                }
        
            
        }
        string final;
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
        cout<<obj.removeConsecutiveDuplicates(s)<<endl;
    }
    
	return 0;
}  // } Driver Code Ends
```