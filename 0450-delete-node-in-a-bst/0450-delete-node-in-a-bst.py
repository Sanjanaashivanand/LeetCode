# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        parent = None
        curr = root

        # Step 1: Find the node to delete
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            return root  # Node not found

        # Helper to find in-order predecessor
        def get_predecessor(node):
            pred_parent = node
            pred = node.left
            while pred.right:
                pred_parent = pred
                pred = pred.right
            return pred, pred_parent

        # Step 2: Delete the node
        def delete_found_node(node, parent):
            # Case 1: No child
            if not node.left and not node.right:
                if not parent:
                    return None
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

            # Case 2: One child
            elif not node.left or not node.right:
                child = node.left if node.left else node.right
                if not parent:
                    return child
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child

            # Case 3: Two children
            else:
                pred, pred_parent = get_predecessor(node)
                node.val = pred.val  # Copy predecessor value

                # Delete the predecessor node
                if pred_parent == node:
                    node.left = pred.left
                else:
                    pred_parent.right = pred.left
            return root

        return delete_found_node(curr, parent)

