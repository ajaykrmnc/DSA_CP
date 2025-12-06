# Sum of progression

problem link: https://codeforces.com/contest/1921/problem/F

```cpp
while(t--){
        int n, q;
        cin>>n>>q;
        int sn = sqrt(n);
        vector<int> v(n);
        for(int i=0;i<n;i++){
            cin>>v[i];
        }
        vector<vector<int>> arr(sn+1, vector<int>(n));
        vector<vector<int>> arr2(sn+1, vector<int>(n));
        for(int i=1;i<=sn;i++){
            arr[i][0] = v[0];
            arr2[i][0] = v[0];
        }
        for(int i=1;i<=sn;i++){
            for(int j=1;j<n;j++){
                arr[i][j] = v[j];
                if(j-i>=0) arr[i][j]+=arr[i][j-i];
            }
        }
        
        for(int i=1;i<=sn;i++){
            for(int j=1;j<n;j++){
                int x = j/i + 1;
                arr2[i][j] = x*v[j];
                if(j-i>=0) arr2[i][j]+=arr2[i][j-i];
            }
        }
        
        debug(arr2)
```