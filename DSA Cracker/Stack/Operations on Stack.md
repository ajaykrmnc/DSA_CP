# Operations on Stack

**Problem Statement:**
Implement basic stack operations including insert (push), remove (pop), find an element, and get the top element (head). The stack follows LIFO (Last In First Out) principle where elements are added and removed from the same end called the top. Push operation adds an element to the top, pop removes the top element, find searches for an element in the stack, and head returns the top element without removing it. These are fundamental stack operations that form the basis for more complex stack-based algorithms and data structure implementations.

```cpp
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++

//Function to push an element into the stack.
void insert(stack<int> &s,int x)
{
    s.push(x);
    
}

//Function to remove top element from stack.
void remove(stack<int> &s)
{
    s.pop();
    
    
    
}

//Function to print the top element of stack.
void headOf_Stack(stack<int> &s)
{
    int x=s.top();
    cout<<x<<" "<<endl; 
}

//Function to search an element in the stack.
bool find(stack<int> s, int val)
{
   bool exists=false;
    
    //traversing while the stack is not empty.
    while(!s.empty())       
    {
        //comparing the top element of stack with given number 
        //to be searched and popping it from stack. 
        int top=s.top();
        s.pop();
        if(top==val)        
        exists=true;
    }
    
    //if element is found, we return true else false.
    if(exists==true){
        return true;
    }
    else{
        return false;
    }

}

// { Driver Code Starts.

int main() {
	int testcases;
	cin>>testcases;
	while(testcases--)
	{
	    stack<int> s;
	    int q;
	    cin>>q;
	    while(q--){
	        char ch;
	        cin>>ch;
	        
	        if(ch=='i')
	        {
	            int x;
	            cin>>x;
	            
	            insert(s,x);
	            
	        }
	        else if(ch=='r')
	        {
	            remove(s);
	        }
	        else if(ch=='h')
	        {
	            headOf_Stack(s);
	        }
	        else if(ch=='f')
	        {
	            int x;
	            cin>>x;
	            if(find(s,x))
	            cout << "Yes";
	            else cout << "No";
	            cout << endl;
	        }
	        
	    }
	}
	return 0;
}
```