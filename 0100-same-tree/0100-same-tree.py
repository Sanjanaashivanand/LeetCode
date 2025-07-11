# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root1, root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val == root2.val:
                return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
            else:
                return False

        return dfs(p, q)
