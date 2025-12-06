# Rudolf and Snowflakes (hard version)

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