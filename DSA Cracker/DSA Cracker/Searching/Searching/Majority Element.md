# Majority Element

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