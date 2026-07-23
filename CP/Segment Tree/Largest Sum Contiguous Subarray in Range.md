# Largest Sum Contiguous Subarray in Range

```cpp
//User function Template for C++

//Function to update a value in input array and segment tree.
node queryhelper(node *st, int li, int hi, int i, int l, int h){
    if(li>=l && hi<=h)
        return st[i];
    node ans;
    if(li>h || hi<l){
        return ans;
    }
    int mid = (li+hi)/2;
    if (l > mid)
        return queryhelper(st, mid+1, hi, 2*i+2, l, h);
    if (h <= mid)
        return queryhelper(st, li, mid, 2*i+1, l, h);
    node left = queryhelper(st, li, mid, 2*i+1, l, h);
    node right = queryhelper(st, mid+1, hi, 2*i+2, l, h);
    ans.sum = left.sum + right.sum;
    ans.prefixsum = max(left.prefixsum, left.sum + right.prefixsum);
    ans.suffixsum = max(right.suffixsum, right.sum + left.suffixsum);
    ans.maxsum = max(ans.prefixsum, max(ans.suffixsum,
                    max(left.maxsum, max(right.maxsum, left.suffixsum + right.prefixsum))));
    return ans;
}

void updatehelper(node *st, int li, int hi, int in, int val, int i){
    if(li==hi){
        st[i].sum = st[i].prefixsum = st[i].suffixsum = st[i].maxsum = val;
        return;
    }
    int mid = (li+hi)/2;
    if(in<=mid)
        updatehelper(st, li, mid, in, val, 2*i+1);
    else
        updatehelper(st, mid+1, hi, in, val, 2*i+2);
    node left = st[2*i+1];
    node right = st[2*i+2];
    st[i].sum = left.sum + right.sum;
    st[i].prefixsum = max(left.prefixsum, left.sum+right.prefixsum);
    st[i].suffixsum = max(right.suffixsum, right.sum+left.suffixsum);
    st[i].maxsum = max(st[i].prefixsum, max(st[i].suffixsum,
                        max(left.maxsum, max(right.maxsum, left.suffixsum+right.prefixsum))));
    return;
}
void update(int arr[], int arrSize, int index, int value)
{
    // code here
    index--;
    arr[index]=value;
    updatehelper(tree,0,arrSize-1,index,value,0);
}

//Funciton to return the Maximum-Sum in the range.
int query(int arr[], int n, int l, int r)
{
    // code here
    l--;
    r--;
    node ans= queryhelper(tree,0,n-1,0,l,r);
    return ans.maxsum;
}
```

