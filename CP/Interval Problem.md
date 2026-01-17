# Interval Problem

**Problem Statement:**
This section contains problems involving intervals and sweep line algorithms. Interval problems typically involve processing ranges or segments on a coordinate system to find overlaps, merge intervals, or calculate properties like maximum overlap count. The sweep line technique processes events (interval start/end points) in sorted order to efficiently solve these problems. Common applications include finding maximum number of overlapping intervals, merging overlapping ranges, and calculating coverage areas. These problems are fundamental in computational geometry and scheduling algorithms.

This technique is useful when you have some intervals and you have to figure out the value of some expression.

—> we will iterate on the x coordinate and try to maintain some important in a data structure.

if we put these 2*n value in a vector a, and sort it, we notice that noting changes between x=a[i] and a[i+1] A[i]=0,a[i+1]=5;

[YouTube](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHdXeVNwRFhzQWxWOGt4c2ladHpITHJPY0M3d3xBQ3Jtc0tscWFWUWctRGZEbG1TYnE4U2l2dFpFQlBXQzVXUU56SmlBaU1EWTVQaXNESEEtdXQwTjVEbWFFZDNxdkZObE5uU2k3X3AtZXVJdExTZjhMclZKZW1KaUtNcXBPdjNHc0VBblMybkVPbm13R3BwRWVTcw&q=https%3A%2F%2Fcodeforces.com%2Fcontest%2F1420%2Fproblem%2FD&v=tgQ3nfemjjQ)

[Problem - E - Codeforces](https://codeforces.com/contest/689/problem/E)

[Problem - E - Codeforces](https://codeforces.com/contest/1106/problem/E)

Sure, here is an implementation of the sweep line technique in C++ for solving the problem [Problem - E - Codeforces](https://codeforces.com/contest/689/problem/E):

```
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> intervals;
    // input intervals as pairs of (start, end) points
    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;
        intervals.push_back({start, end});
    }

    vector<int> events(2*n);
    int index = 0;
    for (auto interval : intervals) {
        events[index++] = interval.first;
        events[index++] = -interval.second;
    }

    sort(events.begin(), events.end(), [](int a, int b) {
        return abs(a) < abs(b);
    });

    int count = 0, ans = 0;
    for (int event : events) {
        if (event >= 0) {
            count++;
        } else {
            count--;
        }
        ans = max(ans, count);
    }

    cout << ans << endl;

    return 0;
}

```

This code takes as input the number of intervals, followed by the start and end points of each interval. It then creates a vector of events by iterating over the intervals and adding their start and end points to the vector. The events are then sorted by their absolute value, which corresponds to their position on the x-axis. The code then iterates over the events, keeping track of the number of intervals that are currently active (i.e. have not ended yet) and updating the maximum number of active intervals seen so far. Finally, the code outputs the maximum number of active intervals seen.

I hope this helps! Let me know if you have any further questions.

![Untitled](Interval%20Problem/Untitled.png)

![Untitled](Interval%20Problem/Untitled%201.png)

![Untitled](Interval%20Problem/Untitled%202.png)

[[🔗 LINK]](https://codeforces.com/contest/689/problem/E) — Problem - E - Codeforces

```cpp

ll N = 200005;
// change this N as required
vll fact(N + 1, 1);
vll ifact(N + 1, 1);
ll C(ll n, ll r)
{
    if (r > n)return 0;
    ll ans = fact[n];
    ans = mod_mul(ans, ifact[r]);
    ans = mod_mul(ans, ifact[n - r]);
    return ans;

}
int main() {
    DIVYA;
    ll t, n, i, j, ans, temp, sum,k,l,r;
    string sans;
    t = 1;
    // cin >> t;
    fo(i, 2, N)
    {
        fact[i] = mod_mul(fact[i - 1], i);
    }
    ifact[N] = inv(fact[N]);
    for (i = N - 1; i > 0; i--)
    {
        ifact[i] = mod_mul(i + 1, ifact[i + 1]);
    }

    while (t--)
    {
        sans = "NO";
        ans = temp = sum = 0;
        cin >> n>>k;
        map<ll,ll>active;
        fo(i,1,n)
        {
        	cin>>l>>r;
        	active[l]++;
        	active[r+1]--;
        }
        vll endpoints;
        for(auto x : active)endpoints.pb(x.first);
        ll curr = 0;
	    	for(int i=0;i<endpoints.size()-1;i++)
	    	{
	    		curr+=active[endpoints[i]];
	    		ll siz = endpoints[i+1] - endpoints[i];
	    		if(curr >= k)
	    		{
	    			ans = (ans + C(curr,k)*siz)%mod;
		    	}
    	}
    	cout<<ans<<"\n";
    }
    return 0;
}
```

[[🔗 LINK]](https://codeforces.com/contest/1106/problem/E) — Problem - E - Codeforces

[Problem - 1884C - Codeforces](https://codeforces.com/problemset/problem/1884/C)