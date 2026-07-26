# Rudolf and CodeVid-23

[Problem - 1846G - Codeforces](https://codeforces.com/problemset/problem/1846/G)

```cpp
struct medicine{
    int day,cure,side;
};

int32_t main() {
    fastio();
    int t=1;
    cin>>t;
    while(t--){
        int n,m;
        cin>>n>>m;
        string s;
        cin>>s;
        int num = stoi(s,nullptr,2);
        debug(num);
        vector<medicine>v(m);
        for(int i=0;i<m;i++){
            cin>>v[i].day;
            string str,str2;
            cin>>str>>str2;
            for(int i=0;i<n;i++){
                if(str[i]=='0'){str[i]='1';}
                else str[i] = '0';
            }
            int num1 = stoi(str,nullptr,2);
            int num2 = stoi(str2,nullptr,2);
            v[i].cure = num1;
            v[i].side = num2;
        }
        vector<long long>dist(1025,LLONG_MAX);
        vector<bool>done(1025);
        dist[num] = 0;
        priority_queue<pair<int,long long>,vector<pair<int,long>>,greater<pair<int,int>>>pq;
        pq.push({0,num});
        while(!pq.empty()){
            int node= pq.top().second;
            pq.pop();
            for(auto [day,cure,side]: v){
                int newcure = (side | (cure & node));
                debug(newcure);
                if(dist[newcure] > dist[node] + day){
                    dist[newcure] = dist[node]+day;
                    pq.push({dist[newcure],newcure});
                }
            }
        }
        debug(dist);
        if(dist[0]== LLONG_MAX){
            cout<<-1<<nline;
        }else{
            cout<<dist[0]<<nline;
        }
    }
    return 0;

}
```