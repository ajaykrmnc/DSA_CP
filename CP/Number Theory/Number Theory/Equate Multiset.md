# Equate Multiset

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