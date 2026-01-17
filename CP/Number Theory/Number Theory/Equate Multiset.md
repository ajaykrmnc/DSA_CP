# Equate Multiset

**Problem Statement:**
Given two multisets A and B of equal size, determine if you can make them equal by performing operations on B. The allowed operation is to replace any element x in B with x/2 (only if x is even). The key insight is to reduce all numbers to their odd parts by dividing by 2 repeatedly. Then use a greedy approach: for each element in B (processed in descending order), try to match it with an element in A by repeatedly dividing by 2 until a match is found or the element becomes odd.

problem link: https://codeforces.com/contest/1702/problem/F

```cpp

        int n;
        cin>>n;
        multiset<int>v,vec;
        for(int i=0;i<n;i++){
            int x;
            cin>>x;
            while(x%2==0){
                x/=2;
            }
            v.insert(x);
        }
        for(int i=0;i<n;i++){
            int x;
            cin>>x;
            while(x%2==0){
                x/=2;
            }
            vec.insert(x);
        }
        bool flag=1;
        for(int i=n-1;i>=0;i--){
            auto it=vec.end();
            it--;
            int num = *it;
            vec.erase(it);
            int tmp=0;
            while(num >= 1 and tmp ==0){
                if(v.find(num)!=v.end()){
                    v.erase(v.find(num));
                    tmp =1;
                }else{
                    num/=2;
                }
            }
            if(tmp==0){
                flag=0;
            }
        }
        if(flag){
            cout<<"YES"<<nline;
        }else{
            cout<<"NO"<<nline;
        }

    }
```