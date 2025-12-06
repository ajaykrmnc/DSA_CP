# Sort an array according to the other

Given two integer arrays **A1[ ]** and **A2[ ]** of size **N** and **M** respectively. Sort the first array **A1[ ]** such that all the relative positions of the elements in the first array are the same as the elements in the second array **A2[ ]**.See example for better understanding.**Note**: If elements are repeated in the second array, consider their first occurance only.

```cpp
//User function template in C++

class Solution{
    public:
    // A1[] : the input array-1
    // N : size of the array A1[]
    // A2[] : the input array-2
    // M : size of the array A2[]
    
    //Function to sort an array according to the other array.
    vector<int> sortA1ByA2(vector<int> arr1, int N, vector<int> arr2, int M) 
    {
        //Your code here
        unordered_map<int,int>index;
        for(int i = 0;i<arr2.size();i++){
            if(index[arr2[i]]==0){
                index[arr2[i]] = i+1;
            }
        }
        
        // lambda comperator fucntion that sorts arr1 based on order 
        // defined by arr2
        auto comp = [&](int a,int b){
            if(index[a] == 0 and index[b] == 0) return a<b;
            if(index[a] == 0) return false;
            
            if(index[b] == 0) return true;
            return index[a] < index[b];
        };
        sort(arr1.begin(),arr1.end(),comp);
        return arr1;
    } 
};
```