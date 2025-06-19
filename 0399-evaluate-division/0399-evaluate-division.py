from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        # Build the graph
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1.0 / val

        def dfs(start, end, visited):
            if start == end:
                return 1.0
            visited.add(start)

            for neighbor in graph[start]:
                if neighbor in visited:
                    continue
                intermediate = dfs(neighbor, end, visited)
                if intermediate != -1.0:
                    # Memoize the result!
                    graph[start][end] = graph[start][neighbor] * intermediate
                    graph[end][start] = 1.0 / graph[start][end]
                    return graph[start][end]

            return -1.0

        results = []
        for start, end in queries:
            if start not in graph or end not in graph:
                results.append(-1.0)
            elif end in graph[start]:
                results.append(graph[start][end])
            else:
                visited = set()
                results.append(dfs(start, end, visited))

        return results
