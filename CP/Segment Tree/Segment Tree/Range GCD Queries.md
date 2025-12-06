# Range GCD Queries

```cpp
// User function template in C++

// st : segment tree
// n : size of the given array
// l and r : range to find gcd i.e L and R respectively

class Solution
{
    public:
    //Function to find gcd of given range.
    int gcdUtil(int l,int r,int st[],int ss,int se,int si){
        if(r<ss or l>se){return 0;}
        if(l<=ss and r>=se){return st[si];}
        int mid= (ss+se)/2;
        return gcd(gcdUtil(l,r,st,ss,mid,2*si+1),gcdUtil(l,r,st,mid+1,se,2*si+2));
    }
    int findRangeGcd(int l, int r, int st[], int n) 
    {
        // code here
        gcdUtil(l,r,st,0,n-1,0);
    }
    void update(int idx,int val,int ss,int se,int si,int st[]){
        if(idx<ss or idx>se){
            return ;
        }else if(ss==se){
            st[si]=val;
            return;
        }
        int mid = (ss+se)/2;
        update(idx,val,ss,mid,2*si+1,st);
        update(idx,val,mid+1,se,2*si+2,st);
        st[si]=gcd(st[si*2+1],st[si*2+2]);
    }
    //Function to update a value in input array and segment tree.
    void updateValue(int index, int new_val, int *arr, int st[], int n) 
    {
        // code here
        arr[index]=new_val;
        update(index,new_val,0,n-1,0,st);
        
    }
};
```