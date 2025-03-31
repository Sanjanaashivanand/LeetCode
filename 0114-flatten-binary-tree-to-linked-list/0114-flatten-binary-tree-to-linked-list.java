class Solution {
    // Helper function to recursively flatten the binary tree
    public void dfs(TreeNode node) {
        if (node == null) return;
        
        // If the node has a left child, we need to process it
        if (node.left != null) {
            // Recursively flatten the left subtree
            dfs(node.left);

            // Save the right subtree to a temporary variable
            TreeNode temp = node.right;

            // Move the left subtree to the right
            node.right = node.left;
            node.left = null;

            // Find the end of the new right subtree (which was originally the left subtree)
            while (node.right != null) {
                node = node.right;
            }

            // Attach the original right subtree to the end of the new right subtree
            node.right = temp;
        }

        // Recursively flatten the right subtree (if not already processed)
        dfs(node.right);
    }

    public void flatten(TreeNode root) {
        dfs(root); // Call dfs to flatten the tree in-place
    }
}
