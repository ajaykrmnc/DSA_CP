# E - Knapsack II

**Problem Statement:**
There are N items, numbered 1, 2, ..., N. For each i (1 ≤ i ≤ N), Item i has a weight of w_i and a value of v_i.
Taro has decided to choose some of the N items and carry them home in a knapsack. The capacity of the knapsack is W,
which means that the sum of the weights of items taken must be at most W. Find the maximum possible sum of the values
of items that Taro takes home. This is a variation of the classic knapsack problem where W can be very large (up to 10^9)
but the values are small (up to 10^3), requiring a different DP approach based on values rather than weights.

```cpp
const int N = 1000005;
int vec[105][2];
int dp[105][100005];

int fun(int ind, int valueleft)
{
    if (valueleft == 0)
        return 0;
    if (ind < 0)
        return 1e15;
    if(dp[ind][valueleft]!=-1)
    return dp[ind][valueleft];

    int ans = fun(ind - 1, valueleft);
    if(valueleft-vec[ind][1]>=0)
    ans = min(ans, fun(ind - 1, valueleft - vec[ind][1])+vec[ind][0]);
    return dp[ind][valueleft]=ans;
}

int32_t main()
{
    speed()
    memset(dp, -1, sizeof(dp));
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        cin >> vec[i][0] >> vec[i][1];
        
    }
    
    int sum=100005;
    for (int i = sum; i >=0; i--)
    {
        if (fun(n - 1, i) <= m)
        {
            cout << i << nline;
            break;
        }
    }

    return 0;
}
```