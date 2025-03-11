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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while(!q.isEmpty()){
            TreeNode rightSide = null;
            int qLen = q.size(); 

            for(int i=0; i<qLen; i++){
                TreeNode curr = q.poll();
                if(curr!=null){
                        rightSide = curr;
                        q.add(curr.left);
                        q.add(curr.right);
                    }
            }

            if(rightSide!=null){
                res.add(rightSide.val);
            }

        }

        return res;
    }
}