# Smaller on Right

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