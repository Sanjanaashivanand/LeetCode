class Solution(object):
    def maxOperations(self, nums, target):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = len(nums)-1
        res = 0

        while l<r:
            total = nums[l] + nums[r]

            if total == target:
                res+=1
                l+=1
                r-=1
            elif total > target:
                r-=1
            else:
                l+=1

        return res
        