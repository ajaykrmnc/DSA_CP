# 1361. Validate Binary Tree Nodes

You have `n` binary tree nodes numbered from `0` to `n - 1` where node `i` has two children `leftChild[i]` and `rightChild[i]`, return `true` if and only if **all** the given nodes form **exactly one** valid binary tree.

If node `i` has no left child then `leftChild[i]` will equal `-1`, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/08/23/1503_ex1.png)

```
Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
```

```cpp
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, std::vector<int>& rightChild) {
        std::unordered_map<int, std::vector<int>> graph;
        std::vector<int> in_degree(n, 0);

        for (int node = 0; node < n; ++node) {
            int left = leftChild[node];
            int right = rightChild[node];
            if (left != -1) {
                graph[node].push_back(left);
                in_degree[left]++;
            }
            if (right != -1) {
                graph[node].push_back(right);
                in_degree[right]++;
            }
        }

        std::vector<int> root_candidates;
        for (int node = 0; node < n; ++node) {
            if (in_degree[node] == 0) {
                root_candidates.push_back(node);
            }
        }

        if (root_candidates.size() != 1) {
            return false;
        }
        int root = root_candidates[0];

        queue<int> q;
        unordered_set<int> seen;
        q.push(root);
        seen.insert(root);

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            if (graph.find(node) != graph.end()) {
                for (int child : graph[node]) {
                    if (seen.find(child) != seen.end()) {
                        return false;
                    }
                    seen.insert(child);
                    q.push(child);
                }
            }
        }

        return seen.size() == n;
    }
};
```