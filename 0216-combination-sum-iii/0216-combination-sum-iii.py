class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path, curr_sum):
            if len(path) == k:
                if curr_sum == n:
                    res.append(list(path))
                return
            
            for i in range(start, 10):
                if curr_sum + i > n:
                    break
                path.append(i)
                backtrack(i + 1, path, curr_sum + i)
                path.pop()

        backtrack(1, [], 0)
        return res