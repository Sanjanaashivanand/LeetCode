# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0

            if root.right==None and root.left!=None:
                return 1 + dfs(root.left)
            elif root.left==None and root.right!=None:
                return 1 + dfs(root.right)
            
            return 1 + min(dfs(root.left), dfs(root.right))
                
        
        return dfs(root)
        