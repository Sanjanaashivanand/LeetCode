# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == val:
                return node

            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)
        
        return None
            
