# Check if two arrays are equal or not

```cpp
//User function template for C++

class Solution{
    public:

    //Function to check if two arrays are equal or not.
    bool check(vector<ll> a, vector<ll> b, int n) {
        //code here
        int ans=1;
        
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        
        for(int i=0;i<n;i++){
            if(a[i]!=b[i]){
                ans  = 0;
                break;
            }
        }
        
        
        return ans;
        
        
    }
};
```