# D. Moscow Gorrillas

**Problem Statement:**
Given two permutations of length n, count the number of segments [l, r] such that the elements in both permutations
within this segment form the same set of consecutive integers. This means for any valid segment, if we take positions l
to r in both permutations, the union of elements should be exactly {min_element, min_element+1, ..., max_element}. Use
the two-pointer technique to maintain the current segment and expand it as needed while counting valid segments
efficiently.

spoiderMan code

```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
  long long t=1;
  while(t--)
  {
    long long n;
    cin>>n;
    long long arr1[n],arr2[n],pos1[n],pos2[n],ans=1,l,r;
    for(long long a=0;a<n;a++)
    {
      cin>>arr1[a];
      pos1[arr1[a]-1]=a;
    }
    for(long long a=0;a<n;a++)
    {
      cin>>arr2[a];
      pos2[arr2[a]-1]=a;
    }
    l=min(pos1[0],pos2[0]);
    r=max(pos1[0],pos2[0]);
    ans+=(l*(l+1))/2;
    ans+=((r-l-1)*(r-l))/2;
    ans+=((n-r-1)*(n-r))/2;
    for(long long a=1;a<n;a++)
    {
      bool c=true;
      if(pos1[a]>=l&&pos1[a]<=r)
      {
        c=false;
      }
      if(pos2[a]>=l&&pos2[a]<=r)
      {
        c=false;
      }
      if(c)
      {
        long long x=-1,y=n;
        if(pos1[a]<l)
          x=max(x,pos1[a]);
        else
          y=min(y,pos1[a]);
        if(pos2[a]<l)
          x=max(x,pos2[a]);
        else
          y=min(y,pos2[a]);
        ans+=(l-x)*(y-r);
      }
      if(pos1[a]<l)
        l=pos1[a];
      else if(pos1[a]>r)
        r=pos1[a];
      if(pos2[a]<l)
        l=pos2[a];
      else if(pos2[a]>r)
        r=pos2[a];
    }
    cout<<ans<<endl;
  }
  return 0;
}
```

