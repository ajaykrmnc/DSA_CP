# Linear Probing in Hashing

```cpp
class Solution{
  public:
    //Function to fill the array elements into a hash table 
    //using Linear Probing to handle collisions.
    vector<int> linearProbing(int hashSize, int arr[], int n)
    {
        //Your code here
        vector<int>hash(hashSize,-1);
        int size = 0;
        for(int i=0;i<n;i++){
            if(size< hashSize){
                int temp = arr[i]%hashSize;
                int j = temp;
                while(hash[j]!=-1 and hash[j]!= arr[i]){
                    j = (j+1)%hashSize;
                }
                if(hash[j]==-1){
                    hash[j] = arr[i];
                    size++;
                }
            }else{
                    break;
                    return hash;
            }
        }
        return hash;
    }
```