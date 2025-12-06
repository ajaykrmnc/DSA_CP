# Maximum Occuring Character

```cpp
class Solution
{
    public:
    //Function to find the maximum occurring character in a string.
    char getMaxOccuringChar(string str)
    {
        //basic without map solution
        int arr[26]={0};//initially all 0 in array of all chars a-z
        
        for(int i=0 ; i<str.length() ; i++){
            char ch=str[i]; // characters of given string
            int count=0;
            count = ch-'a'; //alphabet position in count of that char
            
            //increment the  value as count index in arr[]
            arr[count]++; // do increments the same chars if repeats in string using loop 
        }
        //find max occuring
        int max=-1, ans=0;
        
        for(int i=0 ; i<26 ; i++){
            if(max < arr[i])
            {
                max=arr[i];
                ans=i;
            }
        }
       return  'a' + ans; // get the actual char
        
    }

};
```