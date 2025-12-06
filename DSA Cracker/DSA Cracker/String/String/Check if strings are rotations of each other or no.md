# Check if strings are rotations of each other or not

```cpp
class Solution
{
    public:
    //Function to check if two strings are rotations of each other or not.
    bool areRotations(string s1,string s2)
    {
        if(s1.length() != s2.length()) {
            return false;
        }
        
        string str = s1 + s1;   
        
        if(str.find(s2) != -1) {
            return true;
        }
        
        else {
            return false;
        }
    }
};
```