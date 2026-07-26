# 133. Clone Graph

**Problem Statement:**
Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node contains
a value and a list of neighbors. Use DFS or BFS with a hash map to track visited nodes and their clones. For each node,
create a clone if not already created, then recursively clone all neighbors. The key insight is to maintain a mapping
between original nodes and their clones to avoid infinite loops and ensure each node is cloned exactly once. Time complexity
is O(V + E) where V is vertices and E is edges, and space complexity is O(V) for the hash map and recursion stack.

Given a reference of a node in a [**connected**](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph) undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}

```

```cpp
class Solution {
    public:
    Node* dfs(Node* cur,unordered_map<Node*,Node*>& mp){
        vector<Node*> neighbour;
        Node* clone=new Node(cur->val);
        mp[cur]=clone;
            for(auto it:cur->neighbors)
            {
                if(mp.find(it)!=mp.end()){   //already clone and stored in map
                    neighbour.push_back(mp[it]);    //directly push back the clone node from map to neigh
                }
                else
                    neighbour.push_back(dfs(it,mp));
            }
            clone->neighbors=neighbour;
            return clone;
    }
    Node* cloneGraph(Node* node) {
        unordered_map<Node*,Node*> mp;
        if(node==NULL)
            return NULL;
        if(node->neighbors.size()==0)   //if only one node present no neighbors
        {
            Node* clone= new Node(node->val);
            return clone; 
        }
        return dfs(node,mp);
    }
};
```