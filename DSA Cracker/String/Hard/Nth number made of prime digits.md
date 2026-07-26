# Nth number made of prime digits
**Problem Statement:**
Find the nth number that contains only prime digits (2, 3, 5, 7). For example, the sequence starts: 2, 3, 5, 7, 22, 23, 25, 27, 32, 33, 35, 37, 52, 53, 55, 57, 72, 73, 75, 77, 222, ... This is essentially a base-4 number system where digits are mapped to {2, 3, 5, 7} instead of {0, 1, 2, 3}. The solution involves determining how many digits the nth number will have, then converting the position within that digit group to the corresponding number using base-4 representation. Time complexity is O(log n) for the conversion process.

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