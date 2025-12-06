# Edit Distance

```cpp
class Solution {
public:
    int dp[501][501];
    int recur(string &s,string &str,int pos,int pos2){
        if(pos2==-1)return pos+1;
        if(pos==-1)return pos2+1;
        if(dp[pos][pos2]!=-1){return dp[pos][pos2];}
        int mini=INT_MAX;
        if(s[pos]==str[pos2]){
            // not replace remove and add
            mini=min(recur(s,str,pos-1,pos2-1),mini);
        }
        // add 
        mini=min(1+recur(s,str,pos,pos2-1),mini);
        // replace 
        mini=min(1+recur(s,str,pos-1,pos2-1),mini);
        // remove 
        mini=min(1+recur(s,str,pos-1,pos2),mini);
        return dp[pos][pos2]=mini;
    }
    int minDistance(string word1, string word2) {
        for(int i=0;i<501;i++){
            for(int j=0;j<501;j++){
                dp[i][j]=-1;
            }
        }
        int n=word1.size();
        int m=word2.size();
        int ans=recur(word1,word2,n-1,m-1);
        return ans;
    }
};
```