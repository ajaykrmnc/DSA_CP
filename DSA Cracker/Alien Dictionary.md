# Alien Dictionary

**Problem Statement:**
A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[]
from the alien language's dictionary, where the words are sorted lexicographically according to the language's rules.
Your task is to determine the correct order of letters in this alien language based on the given words. If the order
is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's
rules. This problem uses topological sorting on a directed graph where edges represent character precedence relationships.

```cpp
// User function Template for C++

class Solution{
    public:
    string findOrder(string dict[], int N, int K) {
        //code here
        vector<int>adj[K];
        for(int i = 0;i < N-1; i++){
            string s = dict[i], s2 = dict[i+1];
            int m = 0 , n = 0;
            while(m < s.size() and n < s2.size()){
                if(s[m] != s2[n]){
                    adj[s[m]-'a'].push_back(s2[n]-'a');
                    break;
                }
                m++; n++;
            }
        }
        vector<int>ind(K);
        for(int i = 0;i < K;i++){
            for(auto it: adj[i]){
                ind[it]++;
            }
        }
        queue<int>q;
        for(int i = 0; i < K; i++){
            if(ind[i] == 0){
                q.push(i);
            }
        }
        vector<int>res;
        while(!q.empty()){
            int a = q.front();
            q.pop();
            res.push_back(a);
            for(auto it: adj[a]){
                ind[it]--;
                if(ind[it] == 0){
                    q.push(it);
                }
            }
        }
        string ans = "";
        for(auto i: res){
            ans+=(i+'a');
        }
        return ans;
    }
};
```