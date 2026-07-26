# Minimum Platforms

**Problem Statement:**
Given arrival and departure times of trains at a railway station, find the minimum number of platforms required so that
no train waits. Each train needs a platform from its arrival time until its departure time.

This is a classic interval scheduling problem that can be solved using a greedy approach. Sort both arrival and
departure times separately, then
use two pointers to simulate the process: increment platform count when a train arrives, decrement when a train departs.
The maximum platforms needed at any point is the answer. Time complexity is O(n log n) due to sorting.

```cpp
class Solution{
public:
  //Function to find the minimum number of platforms required at the
  //railway station such that no train waits.

  int findPlatform(int arr[], int dep[], int n)
  {
    // Your code here
    sort(arr,arr+n);
    sort(dep,dep+n);
    int count = 0;
    int ans = 0;
    int i =0 , j =0;
    while( i < n && j<n ){
      if( arr[i] <= dep[j] ){
        count++;
        ans = max(count,ans);
        i++;
      }
      else if ( arr[i] > dep[j] ){
        count--;
        j++;
      }
    }

    return ans;
  }
};
```
