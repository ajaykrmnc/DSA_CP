# E - Knapsack II

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