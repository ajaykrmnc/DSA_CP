# Implement strstr

```cpp
//Function to locate the occurrence of the string x in the string s.
int strstr(string s, string x)
{
    size_t found=s.find(x);
    if (found != string::npos){
        return found;
    }
    else return -1;

}
```