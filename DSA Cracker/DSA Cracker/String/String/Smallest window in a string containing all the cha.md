# Smallest window in a string containing all the characters of another string

```cpp
class Solution
{
    public:
    //Function to find the smallest window in the string s consisting
    //of all the characters of string p.
    string smallestWindow (string s, string p)
    {
        // Your code here
        int n = p.size();
        int m = s.size();
        vector<int>mp(26,0);
        for(int i = 0; i < n; i++){
            mp[p[i]-'a']++;
        }
        int l=-1;
        vector<int>left(26,0);
        vector<int>right(26,0);
        int min_window_size = INT_MAX;
        string ans="-1";
        int window_start = 0;
        int flag=0;
        for(int i=0;i<m;i++){
            right[s[i]-'a']++;
            if(flag==0){
                int temp = 0;
                for(int j=0;j<26;j++){
                    if(mp[j] > right[j]){
                        temp = 1;
                    }
                }
                if( temp == 0){
                    flag = 1;
                }else{
                    continue;
                }
            }
            while(l < i){
                int temp = s[l+1]-'a';
                if(right[temp]-left[temp] == mp[temp]){
                    break;
                }else{
                    l++;
                    left[temp]++;
                }
            }
            int curr_window_size = (i-l);
            if(curr_window_size < min_window_size){
                min_window_size = curr_window_size;
                window_start = l+1;
            }
        }
        if( min_window_size != INT_MAX){
            ans="";
            for(int i = 0; i < min_window_size; i++){
                ans += s[i+window_start];
            }
        }
        return ans;
    }
```