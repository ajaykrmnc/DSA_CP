# Xor

problem link: https://www.codechef.com/problems/ADVITIYA6

[ADVITIYA6 - Editorial](https://discuss.codechef.com/t/advitiya6-editorial/115887)

```cpp
#include<bits/stdc++.h>
using namespace std;
#pragma GCC optimize ("O3","unroll-loops")
#pragma GCC optimize("inline","-ffast-math")
#pragma GCC target("fma,sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,tune=native")
const int N1 = 500001;
int spr[N1][21];
void bldsp(int a[],int n){
    for(int i=0;i<n;i++)spr[i][0]=a[i];
    for(int j = 1;(1<<j)<=n;j++)
        for(int i = 0;i+(1<<j)-1<n;i++)
            spr[i][j]=(spr[i][j-1])&(spr[i+(1<<(j-1))][j-1]);
}
int quespr(int l,int r){
    int lng = log2l(r-l+1);
    return ((spr[l][lng])&(spr[r-(1<<lng)+1][lng]));
}
int main(){
ios_base::sync_with_stdio(false);
cin.tie(NULL);
int testcase=1;
cin>>testcase;
while(testcase--){
   int n;cin>>n;
   map<int,vector<int>> mp;
   int arr[n+1],prfx[n+1];arr[0]=0;prfx[0]=0;
   for(int i=1;i<=n;i++)cin>>arr[i];
   for(int i=1;i<=n;i++){
      prfx[i]=prfx[i-1]^arr[i];
      mp[prfx[i]].push_back(i);
   }
   int fnlans=0;
   bldsp(arr,n+1);
   for(int i = 1;i<=n;i++){
      int pt=i;
      while(pt<=n){
         int crn = quespr(i,pt);
         int p1=pt,p2=n,ans=pt;
         while(p2>=p1){
            int md = (p1+p2)>>1;
            int er = quespr(i,md);
            if(er>=crn){ans=md;p1=md+1;}
            else p2=md-1;
         }
         int checkinxor = crn^prfx[i-1];
         int lastid = upper_bound(mp[checkinxor].begin(),mp[checkinxor].end(),ans)-mp[checkinxor].begin();
         int firstid = lower_bound(mp[checkinxor].begin(),mp[checkinxor].end(),pt)-mp[checkinxor].begin();
         fnlans+=lastid-firstid;
         pt=ans+1;
      }
   }
   cout<<fnlans<<endl;
   
}
  return 0;
}
```