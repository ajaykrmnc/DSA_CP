# Quadratic Probing in Hashing

**Problem Statement:**
Implement quadratic probing collision resolution technique for hash tables. When a collision occurs at position h(key), probe positions h(key) + 1², h(key) + 2², h(key) + 3², etc. until an empty slot is found. Given an array of elements and a hash table size, insert all elements using quadratic probing. The hash function is typically key % hashSize. If an element already exists at the computed position, skip insertion. This technique helps reduce clustering compared to linear probing but may not find empty slots even when they exist.

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