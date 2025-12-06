# Separate chaining in Hashing

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