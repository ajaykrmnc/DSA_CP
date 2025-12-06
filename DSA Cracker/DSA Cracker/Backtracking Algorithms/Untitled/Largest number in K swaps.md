# Largest number in K swaps

Given a number **K** and string **str** of digits denoting a positive integer, build the largest number possible by performing swap operations on the digits of **str** at most **K** times.

```cpp
class Solution
{
    public:
    //Function to find the largest number after k swaps.
    string ans;
    void recur(string s,int n,int i){
        int sz=s.size();
        ans=max(s,ans);
        if(n==0 or i==sz){
            return;
        }
        recur(s,n,i+1);
        for(int j=i+1;j<sz;j++){
            string str=s;
            if(s[j]>s[i]){
                swap(str[i],str[j]);
                recur(str,n-1,i+1);
            }
        }
    }
    string findMaximumNum(string str, int k)
    {
       ans=str;
       recur(str,k,0);
       return ans;
    }
};
```