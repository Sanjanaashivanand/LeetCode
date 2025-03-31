/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void dfs(TreeNode node){
        if(node==null) return;

        if(node.left!=null){
            dfs(node.left);
            
            TreeNode temp = node.right;
            node.right = node.left;
            node.left = null;

            while(node.right!=null){
                node = node.right;
            }

            node.right = temp;
        }

        dfs(node.right);
    }

    public void flatten(TreeNode root) {
        dfs(root);
    }
}