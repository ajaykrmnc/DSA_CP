# Check if a string is Isogram or not

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