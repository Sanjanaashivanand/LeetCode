class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [0] * n
        prod = 1
        for i in range(0, n):
            prefix[i] = prod
            prod *= nums[i]

        suffix = [0] * n
        prod = 1
        for i in range(n-1, -1, -1):
            suffix[i] = prod
            prod *= nums[i]

        ans = [0] * n
        for i in range(0, n):
            ans[i] = prefix[i] * suffix[i]

        return ans