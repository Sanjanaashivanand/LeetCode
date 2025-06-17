# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def dfs(root, currsum):
            if not root:
                return 0

            currsum += root.val
            count = 0
            
            if currsum - targetSum in prefix:
                count = prefix[currsum - targetSum]

            if currsum not in prefix:
                prefix[currsum] = 0
            
            prefix[currsum]+=1
            
            count += dfs(root.left, currsum)
            count += dfs(root.right, currsum)
            prefix[currsum] -= 1
            return count
    

        prefix = {0: 1}
        return dfs(root, 0)


        
        