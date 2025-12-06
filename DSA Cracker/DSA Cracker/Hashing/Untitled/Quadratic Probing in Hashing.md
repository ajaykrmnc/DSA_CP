# Quadratic Probing in Hashing

```cpp
class Solution{
  public:
    //Function to fill the array elements into a hash table 
    //using Quadratic Probing to handle collisions.
    void QuadraticProbing(vector <int>&hash, int hashSize, int arr[], int n)
    {
        //Your code here
        for(int i=0;i<n;i++){
            int k=arr[i]%hashSize;
            int j=0;
            while(hash[(k+j*j)%hashSize]!=arr[i] and hash[(k+j*j)%hashSize]!=-1){
                j++;
            }
            int res= (k+j*j)%hashSize;
            hash[res]=arr[i];
        }
    }

};
```