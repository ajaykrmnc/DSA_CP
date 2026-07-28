# Implement strstr

**Problem Statement:**
Implement the strstr() function which finds the first occurrence of a substring (needle) in a string (haystack). Return
the index of the first occurrence, or -1 if the substring is not found. This is a classic string matching problem that
can be solved using various algorithms: naive approach O(nm), KMP algorithm O(n+m), or Rabin-Karp O(n+m) average case.
The built-in find() function provides an efficient implementation, but understanding the underlying algorithms is
important for interviews and competitive programming.

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

