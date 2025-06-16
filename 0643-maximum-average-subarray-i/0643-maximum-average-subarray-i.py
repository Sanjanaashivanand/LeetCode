class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = 0
        r = 0

        res = float('-inf')
        window = 0

        while r<len(nums):
            window+=nums[r]

            if r-l+1 == k:
                res = max(res, window/float(k))
                window-=nums[l]
                l+=1

            r+=1
        
        return res
