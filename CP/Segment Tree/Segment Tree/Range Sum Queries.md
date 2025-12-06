# Range Sum Queries

```cpp
// User function template for C++

// arr : given array
// n : size of arr
// index : need to update
// new_val : given value to which we need to update index
// st : constructed segment-tree

//Function to update a value in input array and segment tree.
void update(int idx,int val,int ss,int se,int si,ll *st){
    if(idx< ss or idx>se){
        return;
    }
    if(ss==se){
        st[si] = val;
        return ;
    }
    int mid =getMid(ss,se);
    update(idx,val,ss,mid,2*si+1,st);
    update(idx,val,mid+1,se,2*si+2,st);
    st[si] = st[2*si+1]+ st[2*si+2];
}
void updateValue(int *arr, ll *st, int n, int index, int new_val) 
{
    // add code here
    arr[index] = new_val;
    update(index,new_val,0,n-1,0,st);
}

//Function to return sum of elements in range from index qs (query start)
//to qe (query end).
ll getsumutil(int qs,int qe,int ss,int se,int si,ll *st){
    if(qe<ss or qs>se){
        return 0ll;
    }
    if(qs<=ss and qe>=se){
        return st[si];
    }
    int mid = getMid(ss,se);
    return getsumutil(qs,qe,ss,mid,2*si+1,st)+getsumutil(qs,qe,mid+1,se,2*si+2,st);
}
ll getsum(ll *st, int n, int l, int r)
{
    // add code here
    return getsumutil(l,r,0,n-1,0,st);
    
}
```