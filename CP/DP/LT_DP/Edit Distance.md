# Edit Distance

**Problem Statement:**
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. You have the following three operations permitted on a word: insert a character, delete a character, or replace a character. This is a classic dynamic programming problem also known as the Levenshtein distance. The solution uses a 2D DP table where dp[i][j] represents the minimum edit distance between the first i characters of word1 and the first j characters of word2. The recurrence relation considers all three operations and takes the minimum cost path.

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