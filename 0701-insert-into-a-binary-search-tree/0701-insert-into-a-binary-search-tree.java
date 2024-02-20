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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode newNode = new TreeNode(val);
        
        if(root==null){
            root = newNode;
            return root;
        }
        
        TreeNode temp = root;
        
        while(true){
            if(newNode.val > temp.val){
                if(temp.right==null){
                    temp.right = newNode;
                    return root;
                }
                else{
                    temp = temp.right;
                }
            }
            
            else{
                if(temp.left == null){
                    temp.left = newNode;
                    return root;
                }
                else{
                    temp = temp.left;
                }
            }
        }
    }
        
        
    }