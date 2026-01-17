# Isomorphic Strings

**Problem Statement:**
Two strings are isomorphic if the characters in one string can be replaced to get the other string, maintaining the one-to-one character mapping. For example, "egg" and "add" are isomorphic because 'e' maps to 'a' and 'g' maps to 'd'. However, "foo" and "bar" are not isomorphic because 'o' would need to map to both 'a' and 'r'. The solution involves creating a bidirectional mapping between characters of both strings and ensuring no character maps to multiple characters. Use two hash maps to track the mapping from first string to second and vice versa.

```cpp
class Solution
{
    public:
    //Function to check if two strings are isomorphic.
    bool areIsomorphic(string str1, string str2) {
        int n1 = str1.size(), n2 = str2.size();
        int i = 1;
        char temp1 = str1[0], temp2=str2[0];
        if(n1 != n2){
            return false;
        }
        unordered_map <char, char> mp1, mp2;
        // Checking if str1 is mapped to str2
        for(int i=0; i<n1; i++){
            mp1[str1[i]]=str2[i];
        }
        for(int i=0; i<n1; i++){
            if(mp1[str1[i]] != str2[i]){
                return false;
            }
        }
        // Checking if str2 is mapped to str1
        for(int i=0; i<n1; i++){
            mp2[str2[i]] = str1[i];
        }
        for(int i=0; i<n1; i++){
            if(mp2[str2[i]]!=str1[i]){
                return false;
            }
        }
        return true;
        
    }
};
```