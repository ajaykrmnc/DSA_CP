# Removing consecutive duplicates - 2

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