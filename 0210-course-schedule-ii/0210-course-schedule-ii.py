class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def dfs(node, path_visited):
            visited[node] = True
            path_visited[node] = True

            for next in adj[node]:
                if not visited[next]:
                    if dfs(next, path_visited):
                        return True
                elif path_visited[next]:
                    return True

            path_visited[node] = False
            res.append(node)
            return False
        
        #Adj 
        adj = {}

        for i in range(numCourses):
            adj[i] = []
        
        for v, u in prerequisites:
            adj[u].append(v)
        
        visited = [False] * numCourses
        path_visited = [False] * numCourses
        res = []

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i, path_visited):
                    return []

        return res[::-1]