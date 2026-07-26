# Find Common Nodes in two BSTs

```cpp
class Solution
{
    public:
    //Function to find the nodes that are common in both BST. 
     vector <int> findCommon(Node *root1, Node *root2)
   {
    vector<int>res;
    map<int,int>mp;
    
    stack<Node*>st;
    Node*cptr=root1;
    
    while(!st.empty()||cptr!=NULL)
    {
        if(cptr)
        {
            st.push(cptr);
            mp[cptr->data]++;
            cptr=cptr->left;
        }
        else
        {
            cptr=st.top();
            cptr=cptr->right;
            st.pop();
        }
    }
    
    cptr=root2;
    while(!st.empty()||cptr!=NULL)
    {
        if(cptr)
        {
            st.push(cptr);
            mp[cptr->data]++;
            if(mp[cptr->data]==2)res.push_back(cptr->data);
            cptr=cptr->left;
        }
        else
        {
            cptr=st.top();
            cptr=cptr->right;
            st.pop();
        }
    }
    sort(res.begin(),res.end());
    return res;
    
   }
};

// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    getchar();
    while(t--)
    {
        string s;
        getline(cin,s);
        Node* root1 = buildTree(s);

        getline(cin,s);
        Node* root2 = buildTree(s);
        Solution ob;
        vector <int> res = ob.findCommon(root1, root2);
        for (int i : res)
            cout << i << " ";
        cout<< endl;
    }

	return 1;
}  // } Driver Code Ends
```