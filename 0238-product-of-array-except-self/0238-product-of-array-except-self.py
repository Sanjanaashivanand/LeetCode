class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        ans = []
        for i in range(0, len(nums)):
            ans.append(prod)
            prod = prod * nums[i]
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = prod * ans[i]
            prod = prod * nums[i]

        return ans
        