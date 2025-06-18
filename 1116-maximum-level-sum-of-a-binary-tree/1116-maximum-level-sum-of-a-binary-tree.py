# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque()
        q.append(root)
        max_level = -1
        max_sum = float('-inf')
        k=0
        while q:
            size = len(q)
            k+=1
            level_sum = 0
            for i in range(size):
                node = q.popleft()
                level_sum+=node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = k

        return max_level