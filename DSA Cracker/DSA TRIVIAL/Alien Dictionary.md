# Alien Dictionary

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