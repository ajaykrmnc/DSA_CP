# BOOLEAN  PARENTHESIZATION  PROBLEM (MCM)

```cpp
// User function Template for C++

static int mod=1003;
class Solution{
public:
    int f(int i,int j,int isTrue,string &s,vector<vector<vector<int>>> &dp){
        if(i>j)return 0;
        if(i==j){
            if(isTrue){
                return s[i]=='T';
            }else{
                return s[i]=='F';
            }
        }
        if(dp[i][j][isTrue]!=-1)return dp[i][j][isTrue];
        int ways=0;
        for(int k=i+1;k<=j-1;k=k+2){
            int lt=f(i,k-1,1,s,dp);
            int lf=f(i,k-1,0,s,dp);
            int rt=f(k+1,j,1,s,dp);
            int rf=f(k+1,j,0,s,dp);
            if(s[k]=='&'){
                if(isTrue){
                    ways=(ways+(lt*rt)%mod)%mod;
                }else{
                    ways=(ways+(lt*rf)%mod+(lf*rt)%mod+(rf*lf)%mod)%mod;
                }
            }else if(s[k]=='|'){
                if(isTrue){
                    ways=(ways+(lt*rf)%mod+(rt*lt)%mod+(rt*lf)%mod)%mod;
                }else{
                    ways=(ways+(lf*rf))%mod;
                }
            }else{
                if(isTrue){
                    ways=(ways+(lt*rf)%mod+(lf*rt)%mod)%mod;
                }else{
                    ways=(ways+(lt*rt)%mod+(rf*lf)%mod)%mod;
                }
            }
        }
        return  dp[i][j][isTrue]=ways%mod;
    }

    int countWays(int N, string S){
        // code here
        vector<vector<vector<int>>> dp(N, vector<vector<int>> (N,vector<int> (2,-1)));
        return f(0,S.size()-1,1,S,dp)%mod;
    }
};
```