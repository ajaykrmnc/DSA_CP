# Required Length

**Problem Statement:**
Given a number x and target length n, find the minimum number of operations to make x have exactly n digits. In each operation,
you can multiply x by any of its digits (except 0). If it's impossible to reach exactly n digits, output -1. Use BFS to
explore all possible states (current number, current length) and find the minimum operations to reach target length.
The key insight is that multiplying by larger digits grows the number faster, but you need to be careful about digit choices.
State space can be large, so use pruning and early termination when the number becomes too large.

problem link: https://codeforces.com/contest/1681/problem/D

```cpp
#include<bits/stdc++.h>
using namespace std;
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include"mydebug.h"
#else
#define debug(x)
#endif

#define fastio() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define MOD 1000000007
#define inf 1e18
#define ll long long
#define nline "\n"
#define pb push_back
#define set_bits __builtin_popcountll
#define all(x) (x).begin(), (x).end()
vector<int>dp(20,INT_MAX);
map<long long,int>mp;
void recur(long long n,int need,int steps){
    long long res = n;
    if(mp.find(n)==mp.end()){
        mp[n] = steps;
    }else{
        if(mp[n] <= steps )
        return;
        else {
            mp[n] = steps;
        }
    }
    vector<int>digits;
    while(res > 0){
        digits.push_back(res%10);
        res = res/10;
    }
    // debug(digits);
    int sz = digits.size();
    if((int)sz >= need ){
        dp[sz] = min(dp[sz],steps);
        return;
    }
    debug(n);
    for(auto digit: digits){
        if(digit >= 2){
            recur(n*digit,need,steps+1);
        }
    }
}

int32_t main() {
    fastio();
    int digit;
    long long n;
    cin>>digit>>n;
    recur(n,digit,0);
    if(dp[digit] == INT_MAX){
        cout<<-1<<nline;
    }else{
        int mini = INT_MAX;
        for(int i = digit; i<20; i++){
            mini = min(dp[i],mini);
        }
        cout<<mini<<nline;
    }
    return 0;

}
```