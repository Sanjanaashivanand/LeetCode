class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        q = deque()
        q.append(start)

        visited = [False] * n
        visited[start] = True

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()
                if arr[curr] == 0:
                    return True

                if curr + arr[curr] < n and not visited[curr + arr[curr]]:
                    q.append(curr + arr[curr])
                    visited[curr + arr[curr]] = True

                if curr - arr[curr] >= 0 and not visited[curr - arr[curr]]:
                    q.append(curr - arr[curr])
                    visited[curr - arr[curr]] = True
        
        return False