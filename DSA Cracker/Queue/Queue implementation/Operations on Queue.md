# Operations on Queue

**Problem Statement:**
Implement basic operations on a queue data structure. A queue follows FIFO (First In First Out) principle where elements
are added at the rear and removed from the front. Implement operations like enqueue (add element to rear), dequeue
(remove
element from front), front (get front element without removing), and find (search for an element). This problem tests
understanding of queue operations and their implementation using STL queue or custom implementation with arrays/linked
lists.

```cpp
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:

  //Function to push an element in queue.
  void enqueue(queue<int> &q,int x)
  {
    q.push(x);
  }

  //Function to remove front element from queue.
  void dequeue(queue<int> &q)
  {
    q.pop();
  }

  //Function to find the front element of queue.
  int front(queue<int> &q)
  {
    return q.front();
  }

  //Function to find an element in the queue.
  string find(queue<int> q, int x)
  {
    while(!q.empty())
    {
      if(x==q.front())
      {
        return "Yes";
      }
      q.pop();
    }
    return "No";
  }
};

// { Driver Code Starts.

int main() {
	int testcases;
	cin>>testcases;
	while(testcases--)
	{
	  queue<int> s;
	  int q;
	  cin>>q;
	  Solution ob;
	  while(q--){
	    char ch;
	    cin>>ch;

	    if(ch=='i')
	    {
	      int x;
	      cin>>x;

	      ob.enqueue(s,x);

	    }
	    else if(ch=='r')
	    {
	      ob.dequeue(s);
	    }
	    else if(ch=='h')
	    {
	      cout << ob.front(s) << endl;
	    }
	    else if(ch=='f')
	    {
	      int x;
	      cin>>x;
	      cout << ob.find(s,x) << endl;
	    }

	  }
	}
	return 0;
}

// } Driver Code Ends
```

