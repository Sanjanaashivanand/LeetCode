class Solution(object):
    def distanceK(self, root, target, k):
        graph = defaultdict(list)

        # Step 1: Build undirected graph from tree
        def buildGraph(node, parent):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root, None)

        # Step 2: BFS from target to find nodes at distance k
        visited = set()
        q = deque()
        q.append((target, 0))
        visited.add(target)

        res = []

        while q:
            curr, dist = q.popleft()
            if dist == k:
                res.append(curr.val)
            elif dist < k:
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, dist + 1))

        return res
