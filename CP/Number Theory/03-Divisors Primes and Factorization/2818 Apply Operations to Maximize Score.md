# Apply Operations to Maximize Score

**LeetCode:** [2818. Apply Operations to Maximize Score](https://leetcode.com/problems/apply-operations-to-maximize-score/)  
**Difficulty:** Hard  
**Pattern:** Prime factors + monotonic stack  
**Tags:** Array, Math, Stack, Greedy, Sorting, Monotonic Stack, Number Theory

## Problem

Choose operations to maximize score using prime-score ordering and subarray contribution counts.

## Approach

Compute each number prime score, then use a monotonic stack to count how many subarrays select it as dominant. Process values descending and multiply greedily while operations remain.

## Solution

```cpp
const long long mod = 1e9 + 7;
long long binexp(long long n, int pw) {
    long long ans = 1;
    while(pw) {
        if(pw % 2) {
            ans = (ans * n) % mod;
        }
        n = (n * n) % mod;
        pw /= 2;
    }
    return ans;
}
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int max_ele = *max_element(nums.begin(), nums.end()) + 1;
        int n = nums.size();
        vector<int> spf(max_ele);
        for(int i = 2; i < max_ele; i++) {
            spf[i] = i;
        }
        for(int i = 2; i * i < max_ele; i++) {
            if(spf[i] == i)
            for(int j = i * i; j < max_ele; j += i) {
                if(spf[j] == j) spf[j] = i;
            }
        }
        vector<int> primescore(n);
        for(int i = 0; i < n; i++) {
            int num = nums[i];
            int cnt = 0;
            while(num > 1) {
                int prime = spf[num];
                while((num % prime) == 0) {
                    num /= prime;
                }
                cnt++;
            }
            primescore[i] = cnt;
        }
        vector<pair<int,int>>LeftRight(n);
        stack<int> score, bignum;
        for(int i = 0; i < n; i++) {
            while(score.size() && primescore[score.top()] < primescore[i]) {
                score.pop();
            }
            if(score.size()) {
                LeftRight[i].first = score.top() + 1;
            }else {
                LeftRight[i].first = 0;
            }
            score.push(i);
        }
        while(score.size()) {
            score.pop();
        }
        while(bignum.size()) {
            bignum.pop();
        }
        for(int i = n - 1; i >= 0; i--) {
            while(score.size() && primescore[score.top()] <= primescore[i]) {
                score.pop();
            }
            if(score.size()) {
                LeftRight[i].second = score.top() - 1;
            }else {
                LeftRight[i].second = n - 1;
            }
            score.push(i);
        }
        map<int,long long> mp;
        for(int i = 0; i < n; i++) {
            auto &[l, r] = LeftRight[i];
            long long sum = (long long)(i - l) * (long long)(r - i);
            sum += (long long)(r - l + 1);
            mp[-nums[i]] += sum;
        }
        long long ans = 1;
        for(auto [val, cnt]: mp) {
            long long mini = min(cnt, (long long)k);
            k -= mini;
            ans = (ans * (long long)binexp((long long)-val, mini)) % mod;
            if(k == 0) break;
        }
        return ans;
    }
};
```

## Submission

- Status: Accepted
- Language: C++
- Runtime: 347 ms
- Memory: 260.2 MB
