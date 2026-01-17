# Check if a string is Isogram or not
**Problem Statement:**
An isogram is a word or phrase without a repeating letter. Given a string, determine if it is an isogram or not. For example, "programming" is not an isogram because 'r', 'g', and 'm' appear more than once, while "python" is an isogram as all characters are unique. The solution can use a HashSet to track seen characters - if the set size equals string length, it's an isogram. Alternatively, use a frequency array or boolean array for ASCII characters. Time complexity is O(n) and space complexity is O(1) for ASCII characters or O(k) for k unique characters.

```cpp

class Solution
{
    //Function to check if a string is Isogram or not.
    static boolean isIsogram(String data){
        //Your code here
        char str[]=data.toCharArray();
        HashSet<Character> s=new LinkedHashSet<>(str.length-1);
        for(char x:str){
            s.add(x);
        }
        if(data.length()==s.size()){
            return true;
        }
        else
            return false;
}
```