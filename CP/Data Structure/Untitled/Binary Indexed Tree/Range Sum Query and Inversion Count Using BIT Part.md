# Range Sum Query and Inversion Count Using BIT | Part 2

### 

![Untitled](Range%20Sum%20Query%20and%20Inversion%20Count%20Using%20BIT%20Part/Untitled.png)

![Untitled](Range%20Sum%20Query%20and%20Inversion%20Count%20Using%20BIT%20Part/Untitled%201.png)

```cpp
#include<bits/stdc++.h>
using namespace std;

#define int long long

const int N = 1e6 + 10;

int n, a[N], bit[N];

void upd(int x, int v){
    for(int i = x; i <= n; i += i & -i)
        bit[i] += v;
}

int query(int x){
    int sum = 0;
    for(int i = x; i > 0; i -= i & -i)
        sum += bit[i];
    return sum;
}

int inv_cnt(){
    int cnt = 0;
    for(int i = n; i >= 1; --i){
        cnt += query(a[i] - 1);
        upd(a[i], 1);
    }
    return cnt;
}

signed main(){
    cin >> n;
    for(int i = 1; i <= n; ++i)
        cin >> a[i];
    cout << inv_cnt() << endl;
    return 0;
}
```

<aside>
💡 Make an array by taking element as an index

</aside>

![Untitled](Range%20Sum%20Query%20and%20Inversion%20Count%20Using%20BIT%20Part/Untitled%202.png)

<aside>
💡 Process from the left increase the inversion count by index 8 to max=10 .

</aside>

![Untitled](Range%20Sum%20Query%20and%20Inversion%20Count%20Using%20BIT%20Part/Untitled%203.png)

<aside>
💡 then increase the count of 8 by 1

</aside>

<aside>
💡 May be array compression can be used to assign index to array element

</aside>

An alternative approach to array compression in C++ is to use a `map` data structure. This allows us to assign indices to array elements without changing their order. Here is an example implementation:

```
vector<int> compress(vector<int>& a){
    map<int, int> mp;
    for(int x : a){
        mp[x];
    }
    int idx = 1;
    for(auto& p : mp){
        p.second = idx++;
    }
    vector<int> compressed(a.size());
    for(int i = 0; i < a.size(); ++i){
        compressed[i] = mp[a[i]];
    }
    return compressed;
}
```

Here, the `compress` function takes an input vector `a` and returns a new vector `compressed` where each element represents the index of the corresponding element in the compressed version of `a`. The `map` data structure is used to assign indices to array elements. The `idx` variable is used to keep track of the current index as we iterate over the elements in `mp`. Finally, we use a loop to populate the `compressed` vector with the compressed indices.

Note that this approach has a higher time complexity than the previous one, as it involves iterating over the `a` array multiple times and also has the overhead of using a `map`. However, it has the advantage of preserving the original order of the array elements.

![Untitled](Range%20Sum%20Query%20and%20Inversion%20Count%20Using%20BIT%20Part/Untitled%204.png)

![Untitled](Range%20Sum%20Query%20and%20Inversion%20Count%20Using%20BIT%20Part/Untitled%205.png)

![Untitled](Range%20Sum%20Query%20and%20Inversion%20Count%20Using%20BIT%20Part/Untitled%206.png)

```cpp

```