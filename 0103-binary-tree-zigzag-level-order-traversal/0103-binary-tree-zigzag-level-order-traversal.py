# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []

        q = deque()
        q.append(root)
        level = 1

        while q:
            size = len(q)
            level_nodes = []

            for _ in range(0, len(q)):
                node = q.popleft()
                level_nodes.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level%2!=0:
                res.append(level_nodes)
            else:
                res.append(level_nodes[::-1])
            level+=1

        return res