# Range Longest Correct Bracket Subsequence Queries

```cpp
// User function template for C++

class Solution
{
    public:
    // str : given string
    // n : length of the string
    // qs and qe are L and R respectively
    // st : segment tree of the given string of Node type
    // return the maximum length of correct bracket subsequence of the sequence.
    
    //Function to returns the maximum length of correct bracket subsequence
    //between starting and ending indexes.
    Node helper(Node *st,int qs,int qe,int ss,int se,int si){
        if(se<qs or qe<ss){
            Node nullNode;
            return nullNode;
        }
        if(qs<=ss and qe>=se )return st[si];
        int mid = (ss+se)/2;
        Node left= helper(st,qs,qe,ss,mid,2*si+1);
        Node right= helper(st,qs,qe,mid+1,se,2*si+2);
        Node res= merge(left,right);
        return res;
    }
    int getLongestSequence(Node* st, string str, int qs, int qe, int n) 
    {
        // add code here
        Node res  = helper(st,qs,qe, 0, n-1,0);
        return res.pairs*2;
    }
};
```