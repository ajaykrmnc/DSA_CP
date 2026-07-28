# Children Sum Parent

**Problem Statement:**
Given a binary tree, check if it satisfies the children sum property. In this property, for every node, the value of the node should be equal to the sum of values of its left and right children. For leaf nodes, this property is considered satisfied. Use recursive approach to check each node: if it's a leaf, return true; otherwise, calculate the sum of children and compare with the node's value. The solution should handle cases where a node has only one child by considering the missing child as having value 0.

```cpp
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// Tree Node
struct Node {
    int data;
    Node* left;
    Node* right;
};

// Utility function to create a new Tree Node
Node* newNode(int val) {
    Node* temp = new Node;
    temp->data = val;
    temp->left = NULL;
    temp->right = NULL;

    return temp;
}

// Function to Build Tree
Node* buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N') return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;) ip.push_back(str);

    // Create the root of the tree
    Node* root = newNode(stoi(ip[0]));

    // Push the root to the queue
    queue<Node*> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node* currNode = queue.front();
        queue.pop();

        // Get the current node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current node
            currNode->left = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size()) break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current node
            currNode->right = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}

 // } Driver Code Ends
/*Complete the function below

struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
*/

class Solution{
    public:
    //Function to check whether all nodes of a tree have the value 
    //equal to the sum of their child nodes.
    // int isSumProperty(Node *root)
    // {
    //     if(!root) return 1;
    //     if(!root->left&&!root->right) return 1;
    //     if(!root->left) {
    //         if(root->right->data!=root->data)
    //         return 0;
    //     }
    //     if(!root->right)
    //     {
    //         if(root->left->data!=root->data)
    //         return 0;
    //     }
    //     if(root->right->data+root->left->data!=root->data) return 0;
    //     isSumProperty(root->left);
    //     isSumProperty(root->right);
    // }
    int isSumProperty(Node *root){
    if(root==NULL)
        return true;
    if(root->left==NULL && root->right==NULL)
        return true;
    int sum=0;
    if(root->left!=NULL)sum+=root->left->data;
    if(root->right!=NULL)sum+=root->right->data;
    
    return (root->data==sum && isSumProperty(root->left) && isSumProperty(root->right));
     }
};

// { Driver Code Starts.

/* Driver program to test size function*/

  

int main() {

   
    int t;
    scanf("%d ", &t);
    while (t--) {
        string s, ch;
        getline(cin, s);
        
        Node* root = buildTree(s);
        Solution ob;
        cout << ob.isSumProperty(root) << endl;
    }
    return 0;
}
  // } Driver Code Ends
```