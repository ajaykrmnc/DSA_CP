
# Vasiliy's Multiset

```cpp
#include<bits/stdc++.h>
using namespace std;

struct Node{
    Node *Links[2];
    vector<int>cnt = {0,0};
    Node(){
        for(int i=0;i<2;i++){
            Links[i] = NULL;
        }
    }
    bool have(int n){
        return Links[n]!=NULL;
    }
};
class Trie{
    public:
    Node *root = new Node();
    void insertNode(int n){
        Node *node = root;
        for(int i=31;i>=0;i--){
            int res = (((1<<i) & n) > 0) ? 1 : 0;
            if(!node->have(res)){
                Node *newnode = new Node();
                node->Links[res] = newnode;
                node->cnt[res] = 1;
            }else{
                node->cnt[res]++;
            }
            node = node->Links[res];
        }
    }
    void deleteNode(int n){
        Node *node = root;
        for(int i=31;i>=0; i--){
            int res = (((1<<i) & n) > 0) ? 1 : 0;
            if(node->cnt[res]==1){
                node->cnt[res]--;
                delete node->Links[res];
                node->Links[res] = NULL;
                break;
            }else{
                node->cnt[res]--;
                node = node->Links[res];
            }
        }
    }
    int getMaximum(int n){
        Node *node = root;
        int ans = 0;
        for(int i=31;i>=0; i--){
            int res = (((1<<i) & n) > 0) ? 0 : 1;
            if(node->have(res)){
                ans+= (1<<i);
                node = node->Links[res];
            }else{
                node = node->Links[1-res];
            }
        }
        return ans;
    }
};

int32_t main() {
    fastio();
    int n;
    cin>>n;
    Trie Solution;
    for(int i=0;i<n;i++){
        char c;
        cin>>c;
        int m;
        cin>>m;
        string tmp = "done";
        Solution.insertNode(0);
        if( c== '+'){
            Solution.insertNode(m);
            debug(tmp);
        }else if( c=='-' ){
            Solution.deleteNode(m);
            debug(tmp);
        }else if( c=='?'){
            cout<<Solution.getMaximum(m)<<nline;
        }
    }
    return 0;

}
```
