"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None 

        if not node.neighbors:
            return Node(node.val)

        q = deque()
        q.append(node)

        copy = {}
        copy[node] = Node(node.val)

        while q:
            size = len(q)

            for i in range(0, size):
                curr = q.popleft()

                for next in curr.neighbors:
                    if next not in copy:
                        copy[next] = Node(next.val)
                        q.append(next)
                    copy[curr].neighbors.append(copy[next])

        return copy[node]
                    

        