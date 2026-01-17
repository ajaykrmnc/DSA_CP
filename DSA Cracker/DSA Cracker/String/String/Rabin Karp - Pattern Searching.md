# Rabin Karp - Pattern Searching

**Problem Statement:**
Implement the Rabin-Karp algorithm for pattern searching in a text. This algorithm uses hashing to find any one of a set of
pattern strings in a text. The key idea is to compute hash values for the pattern and for each substring of text with the
same length as pattern. If hash values match, then characters are compared. The algorithm uses rolling hash technique to
compute hash values efficiently in O(1) time for each position. Average time complexity is O(n+m) but worst case is O(nm)
when many hash collisions occur. The algorithm is particularly useful for searching multiple patterns simultaneously.

```cpp
//User function Template for C++

// d is the number of characters in the input alphabet 
#define d 256 

//Function to check if the pattern is present in string or not.
bool search(string pat, string txt, int q) 
{ 
	// Your code here
	int n = txt.length();
	int m = pat.length();
	int h=1,p=0,t=0;
	for(int i=0;i<m-1;i++){
	    h = (h*d)%q;
	}
	for( int i=0;i<m;i++){
	    p = (p*d + pat[i])%q;
	    t = (t*d + txt[i])%q;
	}
	for(int i=0;i<=n-m;i++){
	    int j;
	    if( t== p){
	        for(j=0;j<m;j++){
	            if(txt[i+j]!= pat[j]){
	                break;
	            }
	        }
	    }
	    if( j==m ){
	        return true;
	    }
	    if( i <= n-m ){
	        t = (d*(t-h*txt[i]) + txt[i+m ])%q;
	        // if t becomes -ve make it positive by adding q //
	        if (t<0){
	            t = t+q;
	        }
	    }
	}
	return false;
}
```