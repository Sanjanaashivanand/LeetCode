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
    private int res=Integer.MIN_VALUE;

    private int dfs(TreeNode root){
        if(root == null){
            return 0;
        }

        int leftMax = dfs(root.left);
        int rightMax = dfs(root.right);
        leftMax = Math.max(0, leftMax);
        rightMax = Math.max(0, rightMax);

        //Splitting value
        res = Math.max(res, root.val+ rightMax + leftMax);

        return root.val + Math.max(leftMax, rightMax);
    }

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return res;
    }
}