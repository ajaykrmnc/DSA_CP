# Recover Binary Tree

will try to explain the approach using diagrams and pseudo code :

![](https://assets.leetcode.com/users/images/452c1932-e252-4a64-a745-66cb4ef08b1a_1650349299.0155501.jpeg)

![](https://assets.leetcode.com/users/images/66d468cc-dd11-4a36-958d-6ad68956ef96_1650349307.373912.jpeg)

Now try to implement the actual problem.

Hints : Firstly write the inorder traversal and try to follow the array approach of updating the prev,first and second and you will be able to solve it.

Here is my solution :

```kotlin
class Solution {
    TreeNode prev=null,first=null,second=null;
    void inorder(TreeNode root){
        if(root==null)
            return ;
        inorder(root.left);
        if(prev!=null&&root.val<prev.val){
            if(first==null)
                first=prev;
            second=root;
        }
        prev=root;
        inorder(root.right);
    }
    public void recoverTree(TreeNode root) {
        if(root==null)
            return ;
        inorder(root);
        int temp=first.val;
        first.val=second.val;
        second.val=temp;
    }
}
```