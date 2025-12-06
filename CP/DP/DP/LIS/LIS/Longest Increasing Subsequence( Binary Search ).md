# Longest Increasing Subsequence( Binary Search )

```
class Solution{
public:
    int maxLength(string s)
    {
        int n=s.size();
        vector<int>v;
        for(int i=0;i<n;i++){
            auto it=lower_bound(v.begin(),v.end(),int(s[i]));
            if(it==v.end())v.push_back(int(s[i]));
            else {
                int pos=lower_bound(v.begin(),v.end(),int(s[i]))-v.begin();
                v[pos]=int(s[i]);
            }
        }

        return v.size();
    }
};
```