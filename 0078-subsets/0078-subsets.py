class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def backtrack(idx, path):
            if idx == n:
                res.append(path)
                return

            #pick
            backtrack(idx+1, path + [nums[idx]])

            #not pick
            backtrack(idx+1, path)
        
        backtrack(0, [])
        return res
            