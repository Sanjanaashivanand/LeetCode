# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            
            if root1.val == root2.val:
                return isSame(root1.left, root2.left) and isSame(root1.right, root2.right)
            else:
                return False

        def dfs(root):
            if not root:
                return False

            if isSame(root, subRoot):
                return True
            if isSame(root, subRoot):
                return True

            return dfs(root.left) or dfs(root.right)

        return dfs(root)

