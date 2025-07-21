# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        nodes = []
        q = deque()
        q.append((root, 0, 0))  

        while q:
            node, col, row = q.popleft()
            nodes.append((col, row, node.val))

            if node.left:
                q.append((node.left, col - 1, row + 1))

            if node.right:
                q.append((node.right, col + 1, row + 1))

        nodes.sort()

        res = defaultdict(list)
        for col, row, val in nodes:
            res[col].append(val)

        return [res[x] for x in sorted(res)]

