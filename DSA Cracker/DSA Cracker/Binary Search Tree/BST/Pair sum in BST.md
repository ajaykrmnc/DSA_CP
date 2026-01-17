# Pair sum in BST

**Problem Statement:**
Given a Binary Search Tree and a target sum X, determine if there exists a pair of nodes in the BST whose values add up to X. This is the "Two Sum" problem adapted for BST. The solution can use a hash set to store complements while traversing the tree, or use the two-pointer technique on the inorder traversal (which gives sorted order). The hash set approach has O(n) time and space complexity, while the two-pointer approach can be implemented with O(h) space using iterators. Both approaches are more efficient than checking all possible pairs.
Given a BST and a number **X**. The task is to check if any pair exists in BST or not whose sum is equal to X

```cpp
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> set = new HashSet<>();
        return helper(root, set, k);
    }
    private boolean helper(TreeNode root, Set<Integer> set, int target) {
        if (root == null) return false;

        if (set.contains(root.val))return true;
        set.add(target - root.val);

        return helper(root.left, set, target) || helper(root.right, set, target);
    }
}
```