# Two Repeated Elements

```cpp
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution {
  public:
    //Function to find two repeated elements.
    vector<int> twoRepeated (int arr[], int N) {
        int ans=0;
       int size = N+2;
        for(int i=0;i<N;i++){
            ans^=(i+1);
        }
        for(int i=0;i<size;i++){
            ans^=(arr[i]);
        }
        
        int msb=ans&(~(ans-1));
     
        int num1=0,num2=0;
        
        for(int i=0;i<N;i++){
            
            if((i+1)&msb){
                num1^=(i+1);
            }else{
                num2^=(i+1);
            }
        }
        for(int i=0;i<size;i++){
            if(arr[i]&msb){
                num1^=arr[i];
            }else{
                num2^=arr[i];
            }
        }
        int k1=0,k2=0;
        for(int i=0;i<size;i++){
            k1+=arr[i]==num1;
            k2+=arr[i]==num2;
            if(k1==2){
                return {num1,num2};
            }
            if(k2==2){
                return {num2,num1};
            }
        }
        return {1,1};
       
    }
};

// { Driver Code Starts.

int main()
{
    int t,n;
    cin>>t;
    
    while(t--)
    {
        cin>>n;
        
        int a[n+2];
        
        for(int i=0;i<n+2;i++)
            cin>>a[i];
        
        Solution obj;
        vector<int> res;
        res = obj.twoRepeated(a, n);
        cout<<res[0]<<" "<<res[1]<<endl;
    }
    return 0;
}
  // } Driver Code Ends
```