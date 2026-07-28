# Linear Probing in Hashing

**Problem Statement:**
Implement linear probing collision resolution technique in hash tables. When a collision occurs (two keys hash to the same
index), linear probing searches for the next available slot by checking consecutive positions. If position h(key) is occupied,
check h(key)+1, h(key)+2, and so on until an empty slot is found. For insertion, place the element in the first available
slot. For searching, probe until the element is found or an empty slot is encountered. This technique maintains O(1) average
time complexity but can suffer from clustering where consecutive occupied slots form clusters.

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