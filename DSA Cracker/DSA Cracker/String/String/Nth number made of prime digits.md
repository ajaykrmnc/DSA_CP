# Nth number made of prime digits

```cpp
//User function template for C++

class Solution
{
    public:
    //Function to find nth number made of only prime digits.
     int primeDigits(int n)
    {
        //code here
        int i=1;
        int pow4=4;
        int res=0;
        int prime[4]={2,3,5,7};
        
        while(1){
            n=n-pow4;
            if(n<=0){
                n=n+pow4;
                //Digits in res are goint to be "i"
                pow4=pow4/4;
                int x;
                n--;
                while(i--){
                    x=n/pow4;
                    res=res*10+prime[x];
                    n=n-x*pow4;
                    pow4/=4;
                }
                break;
                
            }
            i++;
            pow4*=4;
        }
        
        return res;
    }
};
```