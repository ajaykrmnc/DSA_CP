# Maximum difference between node and its ancestor

```cpp
class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function findMaxDifference(root) {
    let maxDiff = 0;

    function dfs(node, minAncestor, maxAncestor) {
        if (!node) return;

        // Update maxDiff
        maxDiff = Math.max(maxDiff, 
                           Math.abs(minAncestor - node.value), 
                           Math.abs(maxAncestor - node.value));

        // Update min and max for children
        const newMin = Math.min(minAncestor, node.value);
        const newMax = Math.max(maxAncestor, node.value);

        // Recursive calls
        dfs(node.left, newMin, newMax);
        dfs(node.right, newMin, newMax);
    }

    dfs(root, root.value, root.value);
    return maxDiff;
}

// Example usage:
const root = new Node(8);
root.left = new Node(3);
root.right = new Node(10);
root.left.left = new Node(1);
root.left.right = new Node(6);
root.left.right.left = new Node(4);
root.left.right.right = new Node(7);
root.right.right = new Node(14);
root.right.right.left = new Node(13);

console.log(findMaxDifference(root)); // Output: 13
```

This optimized solution uses a depth-first search (DFS) approach to traverse the tree once, maintaining the minimum and maximum ancestor values at each step. The time complexity is O(n), where n is the number of nodes in the tree, and the space complexity is O(h), where h is the height of the tree (due to the recursive call stack).