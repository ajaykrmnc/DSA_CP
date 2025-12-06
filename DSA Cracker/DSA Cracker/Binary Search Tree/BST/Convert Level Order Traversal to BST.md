# Convert Level Order Traversal to BST

```cpp
//User function Template for C++
Node *solve(vector<int>&v){
    if(v.size()==0) return NULL;
    Node *root = new Node (v[0]);
    vector<int>r,l;
    for(int i=1;i<v.size();i++){
        if(v[i]<v[0])l.push_back(v[i]);
        else r.push_back(v[i]);
    }
    root->left = solve(l);
    root->right = solve(r);
    return root;
}

//Function to construct the BST from its given level order traversal.
Node* constructBst(int arr[], int n)
{
    // Code here
    vector<int>v;
    for(int i=0;i<n;i++){
        v.push_back(arr[i]);
    }
    return solve(v);
}
```