# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):
            if not root:
                return (0,0)

            left = dfs(root.left)
            right = dfs(root.right)

            #rob
            pick = root.val + left[1] + right[1]

            #not rob
            skip = max(left) + max(right)

            return [pick, skip]

        return max(dfs(root))