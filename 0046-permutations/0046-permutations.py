class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def permute(path, idx):
            if idx == n:
                res.append(list(path))
                return

            for i in range(idx, n):
                path[idx], path[i] = path[i], path[idx]
                permute(path, idx+1)
                path[idx], path[i] = path[i], path[idx]

        
        permute(nums, 0)
        return res

