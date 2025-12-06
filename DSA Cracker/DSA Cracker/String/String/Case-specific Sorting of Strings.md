# Case-specific Sorting of Strings

```cpp
//User function Template for C++

class Solution
{
    public:
    string caseSort(string str, int n)
    {
        vector<int > v1;
        vector<int >v2;
        for(int i=0;i<n;i++)
        {
            if(str[i]>= 'a' && str[i]<='z')
            {
                v1.push_back(str[i]);
            }
            if(str[i]>='A' && str[i]<='Z')
            {
                v2.push_back(str[i]);
            }
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        
        int j=0;
        int k=0;
        string result="";
        for(int i=0;i<n;i++)
        {
            
            if(str[i]>='a' && str[i]<='z')
            {
                result+=v1[j];
                j++;
            }
            if(str[i]>='A' && str[i]<='Z')
            {
                result+=v2[k];
                k++;
            }
        }
        return result;
        
    }
};
```