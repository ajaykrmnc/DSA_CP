# Intersection of two arrays

```cpp
class Solution {
  public:
    // Function to return the count of the number of elements in
    // the intersection of two arrays.
    int NumberofElementsInIntersection(int a[], int b[], int n, int m) {
        // Your code goes here
        
       int count=0;
        sort(a,a+n);
        for(int i=0;i<n;i++){
            if(i>0 && a[i]==a[i-1]) continue;
            for(int j=0;j<m;j++){
                if(a[i]==b[j]){ 
                    count++;
                    break;
                }
            }
        }
        
        return count;
    }

    };
```