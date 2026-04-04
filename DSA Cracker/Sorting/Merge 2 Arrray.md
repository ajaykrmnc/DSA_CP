# Merge 2 Arrray

```cpp
class Solution{
    public:
        //Function to merge the arrays.
        void merge(long long arr1[], long long arr2[], int n, int m) 
        { 
            int p=n-1;
            int q=0;
            while(p>=0 && q<m){
                if(arr1[p]>arr2[q]){
                    int temp=arr1[p];
                    arr1[p]=arr2[q];
                    arr2[q]=temp;
                    // swap(arr1,p, arr2, q);
                }
                else{
                    break;
                }
                p--;
                q++;
            }
            sort(arr1, arr1+n);
            sort(arr2, arr2+m);
        } 
};
```