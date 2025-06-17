# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #left = -1
        #right = 1

        self.max_len = 0

        def dfs(root, dir, curr_len):
            if not root:
                return

            self.max_len = max(curr_len, self.max_len)

            if dir==-1:
                dfs(root.right, 1, curr_len+1)
                dfs(root.left, -1, 1)
            else:
                dfs(root.left, -1, curr_len+1)
                dfs(root.right, 1, 1)

        if root.left:
            dfs(root.left, -1, 1)
        if root.right:
            dfs(root.right, 1, 1)
        return self.max_len

        