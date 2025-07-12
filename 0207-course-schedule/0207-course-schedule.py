class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(node, currPath):
            visited[node] = True
            currPath[node] = True

            for next in adj[node]:
                if not visited[next]:
                    if dfs(next, currPath):
                        return True
                elif currPath[next]:
                    return True

            currPath[node] = False
            return False
        
        #Build adjacency list
        adj = {}

        for i in range(numCourses):
            adj[i] = []

        for v, u in prerequisites:
            adj[u].append(v)

        #Visited 
        visited = [False] * numCourses
        currPath = [False] * numCourses

        #DFS
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i, currPath):
                    return False

        return True