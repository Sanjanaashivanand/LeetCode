# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        res = []

        stack = [root]

        while stack:
            curr = stack.pop()
            res.append(curr.val)

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return res
        