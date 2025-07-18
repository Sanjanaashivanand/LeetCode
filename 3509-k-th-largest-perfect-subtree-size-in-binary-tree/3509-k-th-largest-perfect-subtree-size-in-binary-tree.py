from heapq import heappush, heappushpop, heapify

class Solution(object):
    def kthLargestPerfectSubtree(self, root, k):
        heap = []
        heapify(heap)

        def dfs(node):
            if not node:
                return True, 0, 0  # isPerfect, height, size

            leftPerfect, leftHeight, leftSize = dfs(node.left)
            rightPerfect, rightHeight, rightSize = dfs(node.right)

            if leftPerfect and rightPerfect and leftHeight == rightHeight:
                size = leftSize + rightSize + 1
                if len(heap) < k:
                    heappush(heap, size)
                elif size > heap[0]:
                    heappushpop(heap, size)
                return True, leftHeight + 1, size
            else:
                return False, max(leftHeight, rightHeight) + 1, 0

        dfs(root)
        return heap[0] if len(heap) == k else -1
