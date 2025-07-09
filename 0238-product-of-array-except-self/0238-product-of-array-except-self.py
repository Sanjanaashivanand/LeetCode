
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prod = 1

        prefix = [0] * n
        for i in range(0, n):
            prefix[i] = prod
            prod = prod * nums[i]

        prod = 1

        for i in range(n-1, -1, -1):
            prefix[i] = prefix[i] * prod
            prod *= nums[i]

        return prefix

        