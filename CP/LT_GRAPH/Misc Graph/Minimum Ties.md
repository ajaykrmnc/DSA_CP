# Minimum Ties

**Problem Statement:**
In a round-robin tournament with n teams, each team plays every other team exactly once. Each game results in a win (+1
point), loss (0 points), or tie (0.5 points each). Given that each team must end up with exactly n/2 points, determine
the outcome of each game to minimize the total number of ties. The solution involves constructing a tournament schedule
where teams are arranged optimally to achieve the required point distribution while minimizing ties through strategic
win/loss assignments.

problem link: https://codeforces.com/problemset/problem/1487/C

```cpp
#include <bits/stdc++.h>
using namespace std;
#define pb push_back #define int long long
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define nline '\n'
#define mac(i,x,y) for(int i=(int)x; i<y; i++)
#define speed() ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);

int32_t main()
{
  speed()
  int t;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    map<int,int>mp;
    if(n%2==1)
      for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
          if(mp[i]<n/2){
            cout<<1<<" ";
            mp[i]++;
          }else{
            cout<<-1<<' ';
            mp[j]++;
          }
        }
      }
    else{
      for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
          if(j-i==n/2){
            cout<<0<<" ";
          }
          else if(mp[i]<(n-1)/2){
            cout<<1<<" ";
            mp[i]++;
          }else{
            cout<<-1<<' ';
            mp[j]++;
          }
        }
      }
    }
    cout<<nline;
  }
  return 0;
}
```

