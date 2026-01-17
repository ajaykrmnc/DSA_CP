# Separate chaining in Hashing

**Problem Statement:**
Implement separate chaining collision resolution technique for hash tables. In separate chaining, each slot of the hash table
contains a linked list (or dynamic array) to store multiple elements that hash to the same index. When inserting an element,
compute its hash value and append it to the list at that index. This method handles collisions gracefully and maintains good
performance even with high load factors. The average time complexity for search, insert, and delete operations is O(1 + α)
where α is the load factor (number of elements / table size). This technique is simple to implement and doesn't suffer from clustering.

```cpp
class Solution{
  public:
    //Complete this function
    //Function to insert elements of array in the hashTable avoiding collisions.
    vector<vector<int>> separateChaining(int hashSize,int arr[],int sizeOfArray)
    {
       //Your code here
       vector<vector<int>>sc(hashSize);
       for(int i=0;i<sizeOfArray;i++){
           int key= arr[i]%hashSize;
           sc[key].push_back(arr[i]);
       }
       return sc;
    }
};
```