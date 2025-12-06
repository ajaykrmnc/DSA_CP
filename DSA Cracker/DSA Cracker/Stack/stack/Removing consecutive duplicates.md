# Removing consecutive duplicates

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