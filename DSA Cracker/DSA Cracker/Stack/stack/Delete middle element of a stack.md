# Delete middle element of a stack

**Problem Statement:**
Given a stack, delete the middle element of the stack without using any additional data structure. The middle element is defined as the element at position (size/2 + 1) from the bottom of the stack (1-indexed). You need to implement this using recursion where you pop elements, recursively call the function, and then push back the elements except the middle one. This problem tests your understanding of recursion and stack operations. The solution should maintain the relative order of all other elements while removing only the middle element.

```cpp
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++
int cnt=1;

// class Solution
// {
    // public:
    // //Function to delete middle element of a stack.
    // void helper(stack<int> &newstack,stack<int> s,int mid)
    // {
        
    //     if(s.empty())
    //     return ;
    //     int a=s.top();
    //     s.pop();
    //     helper(newstack,s,mid);
    //     if(cnt!=mid)
    //     newstack.push(a);
    //     cnt++;
    //     return ;
        
        
    // }
    // void deleteMid(stack<int>&s,int n)
    // {
    //     int mid=(ceil(float(n)/2.0));
    //      stack<int>newstack;
    //      helper(newstack,s,mid);
    //      s=newstack;
         
    //     // code here.. 
    // }
    class Solution
{
   public:
   //Function to delete middle element of a stack.
   void deleteMid(stack<int>&s, int sizeOfStack)
   {
       vector<int> res;
       int n = s.size();
       int idx;
       if(n%2==0){
           idx = ceil((n/2));
       }else{
           idx = (n/2);
       }
       
       int count = 0;
       for(int i=0;i<n;i++){
           res.push_back(s.top());
           s.pop();
       }
       
       res.erase(res.begin()+idx);
       
       reverse(res.begin(),res.end());
       for(int i=0;i<res.size();i++){
           s.push(res[i]);
       }
   }
};

// { Driver Code Starts.
int main() {
    int t;
    cin>>t;
    
    while(t--)
    {
        int sizeOfStack;
        cin>>sizeOfStack;
        
        stack<int> myStack;
        
        for(int i=0;i<sizeOfStack;i++)
        {
            int x;
            cin>>x;
            myStack.push(x);    
        }

            Solution ob;
            ob.deleteMid(myStack,myStack.size());
            while(!myStack.empty())
            {
                cout<<myStack.top()<<" ";
                myStack.pop();
            }
        cout<<endl;
    }   
    return 0;
}
  // } Driver Code Ends
```