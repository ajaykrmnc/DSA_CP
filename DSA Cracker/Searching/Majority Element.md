# Majority Element

**Problem Statement:**
Given an array of integers, find the majority element that appears more than n/2 times in the array. The majority element
always exists in the given array. This classic problem can be solved using Boyer-Moore Voting Algorithm in O(n) time and
O(1) space complexity. The algorithm maintains a candidate element and a counter, incrementing counter for same elements and
decrementing for different elements. When counter becomes zero, we update the candidate. The final candidate is guaranteed
to be the majority element due to the problem constraint.

```cpp
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution{
  public:
    int majorityElement(int a[], int n)
    {
        map<int,int>mp;
        for(int i=0;i<n;i++)
        {
            mp[a[i]]++;
        }
        auto it=mp.begin();
        for(it=mp.begin();it!=mp.end();it++)
        {
           if(it->second>ceil(n/2))return it->first;
        }
        return -1;
        
        
        
    }
};

// { Driver Code Starts.

int main(){

    int t;
    cin >> t;

    while(t--){
        int n;
        cin >> n;
        int arr[n];
        
        for(int i = 0;i<n;i++){
            cin >> arr[i];
        }
        Solution obj;
        cout << obj.majorityElement(arr, n) << endl;
    }

    return 0;
}
  // } Driver Code Ends
```