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
    public TreeNode searchBST(TreeNode root, int val) {
        TreeNode temp = root;
        while(true){
            if(val == temp.val){
                return temp;
            }
            else if(val > temp.val){
                if(temp.right==null){
                    return null;
                }
                temp = temp.right;
            }
            else{
                if(temp.left==null){
                    return null;
                }
                temp=temp.left;
            }
        }
        
    }
}