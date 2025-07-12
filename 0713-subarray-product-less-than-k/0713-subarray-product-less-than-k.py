class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        left = 0
        prod = 1

        for right in range(len(nums)):
            prod *= nums[right]

            while left<=right and prod >= k :
                prod = prod // nums[left]
                left+=1

            res += (right - left + 1)

        return res
        