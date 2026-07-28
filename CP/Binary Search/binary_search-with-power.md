# Binary search with power

**Problem Statement:**
Given a number n, determine if it can be represented as 1 + b + b² + ... + b^k for some integers b ≥ 2 and k ≥ 2. This
is essentially checking if n can be written as a geometric series sum. Use binary search on the base b
for each possible length k. For each k, binary search to find if there exists a base b such that the geometric
series equals n. Handle overflow carefully when computing powers.

Problem link: [Codeforces](https://codeforces.com/problemset/problem/1846/E2)

we'll do binary search on power. If power varies from 0 to x, and base can be 1 to n. Binary search from 1 to n, and if
sum is less than req, then l = mid + 1, else high = mid - 1, if sum == req then reqturn 1; we'll do the same for the
every power from 1 to 64

---

```cpp
//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// Function to return minimum number of jumps to end of array

class Solution {
public:
  long long smallestGoodBase(long long n) {
    auto pred = [&](long long mid,int i){
      int flag = 0;
      long long st = 1;
      long long sum = 1;
      for(int j = 0;j < i;j++){
        long long num = n/mid;
        if(st > num){
          return -1;
        }
        st*=mid;
        sum+=st;
      }
      if(sum == n){
        return 1;
      }
      return 0;
    };
    long long finalans = n-1;
    for(int i = 63; i >=2; i--){
      long long lo = 2;
      long long hi = n;
      long long ans = -1;
      while(lo<= hi){
        long long mid = lo + (hi-lo)/2;
        if(pred(mid,i) == -1){
          hi = mid - 1;
        }else if(pred(mid,i) == 0){
          lo = mid + 1;
        }else{
          ans = mid;
          break;
        }
      }
      if( ans != -1){
        finalans = ans;
        break;
      }
    }
    return finalans;
  }
};

//{ Driver Code Starts.

int main()
{
  int t;
  cin>>t;
  while(t--)
  {
    long long n;
    cin>>n;
    Solution obj;
    long long ans = obj.smallestGoodBase(n);
    if(ans == n-1){
      cout<<"NO"<<endl;
    }else{
      cout<<"YES"<<endl;
    }
  }
  return 0;
}

// } Driver Code Ends
```
