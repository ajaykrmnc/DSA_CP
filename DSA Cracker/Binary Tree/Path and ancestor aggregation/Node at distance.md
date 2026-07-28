# Node at distance

**Problem Statement:**
Given a binary tree and an integer k, find the count of nodes that are at exactly distance k from any leaf node. A node
is at distance k from a leaf if there exists a path of length k from that node to some leaf node. Use DFS to find all
leaf nodes and their parent relationships. For each leaf node, traverse k steps upward using parent pointers and mark
all such nodes. Use a set to avoid counting duplicate nodes that are at distance k from multiple leaves. Time complexity
is O(n) where n is the number of nodes.

```cpp
//Node Structure
/*struct Node
{
	int k;
	Node *left, *right;
};*/

//Function to return count of nodes at a given distance from leaf nodes.
unordered_map<Node *,Node*>mp;
vector<Node *>leaf;
set<Node *>ans;
void recur(Node *node, Node *par){
  if(node == NULL){
    return;
  }
  if(node->left == NULL and node->right == NULL){
    leaf.push_back(node);
  }
  mp[node] = par;
  recur(node->left,node);
  recur(node->right,node);
}

int printKDistantfromLeaf(Node* root, int k)
{
	//Add your code here.   mp.clear();
	ans.clear();
	leaf.clear();
	recur(root,NULL);
  int n = leaf.size();
	for(int i = 0; i < n; i++){
	  int cnt = 0;
	  Node *curr = leaf[i];
	  while( cnt < k and curr != NULL ){
	    curr = mp[curr];
	    cnt+=1;
	  }
	  if(cnt == k and curr!= NULL){
	    ans.insert(curr);
	  }
	}
	return ans.size();
}
```

