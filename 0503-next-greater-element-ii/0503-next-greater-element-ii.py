class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = []
        res = [-1] * n  # default: no greater element

        for i in range(2 * n):  # simulate circular array
            real_idx = i % n
            while stack and nums[real_idx] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[real_idx]
            if i < n:  # only push first n elements
                stack.append(real_idx)

        return res
