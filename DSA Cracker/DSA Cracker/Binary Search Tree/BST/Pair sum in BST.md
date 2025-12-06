# Pair sum in BST

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