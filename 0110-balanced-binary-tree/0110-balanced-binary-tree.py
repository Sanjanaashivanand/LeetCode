# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.res = True

        def dfs(root):
            if not root:
                return 0

            #Height left
            l = dfs(root.left)

            #right
            r = dfs(root.right)

            if abs(l-r) > 1:
                self.res = False

            return 1 + max(l, r)

        dfs(root)
        return self.res 
        