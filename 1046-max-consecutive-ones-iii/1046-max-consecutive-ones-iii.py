class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ones = 0
        zeros = 0

        i=0
        j=0

        res = 0

        while i<len(nums) and j<len(nums):
            while j<len(nums) and (nums[j]==1 or zeros<k):
                if nums[j] == 0:
                    zeros += 1
                else:
                    ones += 1
                j+=1

            res = max(res, j-i)
            if nums[i] == 0:
                zeros -= 1
            else:
                ones -= 1
            i+=1

        return res

        