# Smaller on Right

**Problem Statement:**
Given an array of integers, for each element, count how many elements to its right are smaller than it. This problem can be solved using various approaches: brute force O(n²), merge sort with inversion counting O(n log n), or using data structures like BST or Fenwick tree. An efficient approach is to process the array from right to left, maintaining a set of seen elements, and for each element, count how many elements in the set are smaller using binary search. The maximum count across all elements gives the answer.

```cpp
#include<bits/stdc++.h>
using namespace std;
#define nline "\n"

int main() {
	//code
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    vector<int>v(n);
	    for(auto &x: v){
	        cin>>x;
	    }
	    reverse(v.begin(),v.end());
	    set<int>st;
	    int maxi=0;
	    for (int i=0;i<n;i++){
	        st.insert(v[i]);
	        auto tmp=st.lower_bound(v[i]);
	        maxi=max(maxi,int(distance(st.begin(),tmp)));
	    }
	    cout<<maxi<<nline;
	}
	return 0;	
}
```