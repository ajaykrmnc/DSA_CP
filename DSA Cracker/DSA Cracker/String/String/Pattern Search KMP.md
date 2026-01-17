# Pattern Search KMP

**Problem Statement:**
Implement the Knuth-Morris-Pratt (KMP) algorithm for pattern searching in a text. Given a text and a pattern, find all occurrences
of the pattern in the text efficiently. KMP algorithm preprocesses the pattern to create a Longest Proper Prefix which is also
Suffix (LPS) array, which helps skip characters during matching. This avoids the O(nm) time complexity of naive approach and
achieves O(n+m) time complexity. The key insight is that when a mismatch occurs, we don't need to start matching from the beginning
but can use the LPS array to determine the next position to match from.

```cpp
//User function Template for C++

//Function to fill lps[] for given patttern pat[0..M-1].
void computeLPSArray(string pat, int M, int* lps) 
{ 
	// Your code here
	int len = 0;
	lps[0] = 0;
	int i = 1;
	while(i<M){
	    if(pat[i] == pat[len]){
	        len++;
	        lps[i] = len;
	        i++;
	    }else{
	        if(len == 0){
	            lps[i] = 0;
	            i++;
	        }else{
	            len = lps[len-1];
	        }
	    }
	}
} 

//Function to check if the pattern exists in the string or not.
bool KMPSearch(string pat, string txt) 
{
    // Your code here
    int n = txt.length();
    int m = pat.length();
    int lps[m];
    computeLPSArray(pat,m,lps);
    int i = 0;
    int j = 0;
    while(i < n){
        if(pat[j] == txt[i]){
            i++;
            j++;
            if(j == m){
                return true;
            }
        }else if(pat[j] != txt[i]){
            if(j == 0){
                i++;
            }else{
                j = lps[j-1];
            }
        }
    }
    return false;
}
```