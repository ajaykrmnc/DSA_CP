# Range LCM Queries

```cpp
// User function template in C++

// arr : given array
// n : size of the array
// qs and qe are L and R respectively given in the problem to denotes range
// st : segment tree of the array arr

//Function to find LCM of given range.
ll gl(ll *st, int qs , int qe, int ss, int se, int si){
    if(qs > se || qe < ss){
        return 1;
    }
    if(qs <= ss && qe >= se){
        return st[si];
    }
    int mid = ss + (se - ss)/2;
    return LCM(gl(st, qs, qe, ss, mid , 2*si + 1), gl(st, qs, qe, mid + 1, se, 2*si + 2));
}

ll getLCM(ll *st, int *arr, int n, int qs, int qe) 
{
    return gl(st, qs , qe , 0, n - 1, 0);
}

//Function to update a value in input array and segment tree.

void ud(int* arr, ll *st, int ss, int se, int si, int index, int new_val){
    if(index < ss || index > se){
        return;
    }
    if(index == ss && index == se){
        arr[index] = new_val;
        st[si] = new_val;
        return;
    }
    if(ss < se){
        int mid = ss + (se - ss)/2;
        ud(arr, st, ss, mid, 2*si + 1, index, new_val);
        ud(arr, st, mid + 1, se, 2*si + 2, index, new_val);
        st[si] = LCM(st[2*si + 1], st[2*si + 2]);
    }
}

void updateValue(int *arr, ll *st, int n, int index, int new_val)
{
    ud(arr, st, 0, n - 1, 0, index, new_val);
    return;
}
```