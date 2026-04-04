# S - Digit Sum

Tags: digit-dp

# Digit DP

![Untitled](S%20-%20Digit%20Sum/Untitled.png)

### Why iterative?

I learned digit DP few years back but only recently I realised that the recursive solution is sometimes hard to debug and difficult to reason about. So this article aims to provide an iterative solution template that can be extended to solve similar problems.

## The Problem

Find count of numbers in range [L, R] such that sum of its digits is a prime number.

$$
1 <= L,R <= 10^{18}
$$

## Basic Idea

- A brute force approach would be to iterate through each number from L to R and check if sum of its digits is prime. This will obviously timeout as constraints are too large.
- So which particular property can we count such that we don't consume too much time/memory? Sum of digits of numbers! **Sum of digits of a number cannot exceed 180** for 18 digits, thus we will have to track only 180 states which will save time and memory.This is the key idea behind most digit DP problems: identify and track a property which is finite and will help us reach the answer.
- We will try to create a function $f(x)$ which returns all good numbers from $[0,x]$. Later we can use $f(R)-f(L-1)$ to find our answer.

### Detailed Explanation

- Let us declare our dp as follow
    - dp[20][2][200]
    - 20→ maximum no of digits that our dp support
    - 2 → tight condition discussed later discussed
    - 200→ maximum possible sum of digits of a number

- what does $dp[i][tight][sum]$ means
    - $dp[i][0][sum]$  → count of suffixes that can be formed starting from index i, whose digits add up to sum
    - $dp[i][1][sum]$ → count of suffixes that can be formed with index i, whose digit adds up to the sum such that formed suffix is not greater that the corresponding suffix of the given string.
    - 

$$
dp[i][0][sum] = \sum\limits_{d=0}^{9} dp[i+1][0][sum-d]
$$

$$
dp[i][1][sum] = dp[i+1][1][sum-ss[i]] + \sum\limits_{d=0}^{ss[i]-1} dp[i+1][0][sum-d]
$$

# Code

```cpp
int digit_dp(string ss) {
    int n = ss.size();
 
    //empty suffixes having sum=0
    dp[n][0][0] = 1;
    dp[n][1][0] = 1;
 
    for(int i = n-1; i >=0 ; i--) {
        for(int tight = 0; tight < 2 ; tight++) {
            for(int sum = 0; sum < 200 ; sum++) {
                if(tight) {
                    for(int d = 0; d <= ss[i] - '0' ; d++) {
                        dp[i][1][sum] += (d == ss[i]-'0') ? dp[i+1][1][sum-d] : dp[i+1][0][sum-d];
                    }
                }
                else {
                    for(int d = 0; d < 10 ; d++) {
                        dp[i][0][sum] += dp[i+1][0][sum-d];
                    }
                }
            }
        }
    }
    int ans = 0;
    for(int i = 0; i < 200; i++) {
        if(isPrime(i))
	        ans += dp[0][1][i];
    }
    return ans;
}
```

# Complexity

- As obvious from the loops:
    
    $$
    ⁍ 
    $$
    

# End Notes

- Find above SPOJ problem here: [GONE](https://www.spoj.com/problems/GONE/)
- Similar SPOJ problem where you can extend above solution: [RAONE](https://www.spoj.com/problems/RAONE/)
- Recent codeforces problem which requires a similar approach: [https://codeforces.com/contest/1341/problem/D](https://codeforces.com/contest/1341/problem/D)
- Educational Codeforces Digit DP problem: [https://codeforces.com/contest/1036/problem/C](https://codeforces.com/contest/1036/problem/C)
- This is my first article on codeforces. All comments/criticism are welcome.

```cpp
#include<bits/stdc++.h>
using namespace std;
 
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include "mylib/mydebug.h"
#else
#define debug(x)
#endif
 
#define int long long

const int MAXN = 1e4 + 10;
const int mod = 1e9 + 7;

vector<vector<vector<int>>>dp(MAXN, vector<vector<int>>(2, vector<int>(100, 0)));

int digit_dp(string ss, int modd) {
    int n = ss.size();
    //empty suffixes having sum=0
    dp[n][0][0] = 1;
    dp[n][1][0] = 1;
 
    for(int i = n - 1; i >=0; i--) {
        for(int tight = 0; tight < 2 ; tight++) {
            for(int sum = 0; sum < modd ; sum++) {
                if(tight) {
                    for(int d = ss[i] - '0'; d >= 0; d--) {
                        dp[i][1][(sum + d) % modd] += (d == ss[i]-'0') ? dp[i+1][1][sum] : dp[i+1][0][sum];
                        dp[i][1][(sum + d) % modd] %= mod;
                    }
                }
                else {
                    for(int d = 0; d < 10 ; d++) {
                        dp[i][0][(sum + d) % modd] += dp[i+1][0][sum];
                        dp[i][0][(sum + d) % modd] %= mod;

                    }
                }
            }
        }
    }
    int ans = dp[0][1][0] - 1 + mod;
    return ans % mod;
}
 
int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int t = 1;
    // cin >> t;
    while (t--) {
       string str;
       int d;
       cin >> str >> d;
       cout << digit_dp(str, d);
    }
    return 0;
}
```

```cpp
#include<bits/stdc++.h>
using namespace std;
 
#ifdef AJAY
#define debug(x) cerr << #x <<" "; _print(x); cerr << endl;
#include "mylib/mydebug.h"
#else
#define debug(x)
#endif
 
string fun(string str, int d){
    if(str.length() > 0){
        return char(int('0') + d) + str;
    }
    return "";
}
string digit_dp(string ss, string ss2) {
    int n = ss.size();
    int m = ss2.size();
    if(n != m){
        string ts;
		while(n--) ts+='9';
        return ts;
    }
    string dp[n + 1][4][10][10];
    fill(&dp[0][0][0][0], &dp[0][0][0][0] + sizeof(dp) / sizeof(dp[0][0][0][0]), "");
    //empty suffixes having sum=0
    dp[n][0][9][0] = " ";
    // 0 means free any value from 0 to 9
    dp[n][1][9][0] = " ";
    // 1 means 9999... to suffix of lower string
    dp[n][2][9][0] = " ";
    // 2 means between lower string and upper string
    dp[n][3][9][0] = " ";
    // 3 means between suffix of higher string to 0000..
    
    for(int i = n-1; i >=0 ; i--) {
        for(int tight = 0; tight < 4 ; tight++) {
            for(int maxi = 0; maxi < 10; maxi++){
                for(int mini = 0; mini < 10; mini++){
                    if(tight == 2){
                        for(int d = ss[i] - '0'; d <= ss2[i] - '0'; d++){
                            if(dp[i][2][min(mini,d)][max(maxi, d)].size() > 0){
                                continue;
                            }
                            if(d == ss[i] - '0' and ss[i] < ss2[i]){
                                dp[i][2][min(mini, d)][max(maxi, d)] = fun(dp[i + 1][1][mini][maxi], d);
                            }else if(d == ss[i] - '0'){
                                dp[i][2][min(mini, d)][max(maxi, d)] = fun(dp[i + 1][2][mini][maxi], d);
                            }else if(d == ss2[i] - '0'){
                                dp[i][2][min(mini, d)][max(maxi, d)] = fun(dp[i + 1][3][mini][maxi], d);
                            }else{
                                dp[i][2][min(mini, d)][max(maxi, d)] = fun(dp[i + 1][0][mini][maxi], d);
                            }
                        }
                    } else if (tight == 3){
                        for(int d = 0; d <= ss2[i] - '0'; d++){
                            if(dp[i][3][min(mini,d)][max(maxi, d)].size() > 0){
                                continue;
                            }
                            if(d == ss2[i] - '0'){
                                dp[i][3][min(mini,d)][max(maxi, d)] = fun(dp[i + 1][3][mini][maxi], d);
                            }else{
                                dp[i][3][min(mini,d)][max(maxi, d)] = fun(dp[i + 1][0][mini][maxi], d);
                            }
                        }
                    }else if(tight == 1){
                        for(int d = ss[i] - '0'; d <= 9; d++){
                            if(dp[i][1][min(mini,d)][max(maxi, d)].size() > 0){
                                continue;
                            }
                            if(d == ss[i] - '0'){
                                dp[i][1][min(mini, d)][max(maxi, d)] = fun(dp[i + 1][1][mini][maxi], d);
                            }else{
                                dp[i][1][min(mini, d)][max(maxi, d)] = fun(dp[i + 1][0][mini][maxi], d);
                            }
                        }
                    }else{
                        for(int d = 0; d < 10; d++){
                            if(dp[i][0][min(mini,d)][max(maxi, d)].size() > 0){
                                continue;
                            }
                            if(dp[i + 1][0][mini][maxi].size() > 0)
                            dp[i][0][min(mini, d)][max(maxi, d)] = fun(dp[i + 1][0][mini][maxi], d);
                        }
                    }
                }
            }
        }
    }
    for(int k = 0; k < 10; k++){
            for(int l = 0; l < 10; l++){
                cout << dp[0][0][k][l] << " ";
            }
            cout << endl;
        }
    int ans = 10;
    int res = 0;
    string str;
    for(int i = 0; i < 10; i++){
        for(int j = i; j < 10; j++){
            if(dp[0][2][i][j].size() > 0 and ans > j - i){
                ans = j - i;
                str = dp[0][2][i][j];
            }
        
        }
    }
    return str;
}
 
int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int t =1;
    // cin >> t;
    while(t--){
        string ss, ssw;
        cin >> ss >> ssw;
        string ans = digit_dp(ss, ssw);
        cout << ans << endl;
    }
    return 0;
}
```