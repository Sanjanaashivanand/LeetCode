# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root, leaves):
            if not root:
                return

            if not root.left and not root.right:
                leaves.append(root.val)

            dfs(root.left, leaves)
            dfs(root.right, leaves)
            return leaves

        l1 = dfs(root1, [])
        l2 = dfs(root2, [])
        
        if len(l1)!=len(l2):
            return False

        for i, j in zip(l1,l2):
            if i!=j:
                return False
                
        return True
