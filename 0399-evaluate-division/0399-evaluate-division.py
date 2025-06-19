from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        results = []
        for start, end in queries:
            if start not in graph or end not in graph:
                results.append(-1.0)
            elif start == end:
                results.append(1.0)
            else:
                visited = set()
                res = self.dfs(start, end, 1.0, graph, visited)
                results.append(res if res != -1 else -1.0)

        return results

    def dfs(self, current, target, acc, graph, visited):
        if current == target:
            return acc

        visited.add(current)

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                result = self.dfs(neighbor, target, acc * weight, graph, visited)
                if result != -1:
                    return result

        return -1
