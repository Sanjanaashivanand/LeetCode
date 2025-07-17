class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = 0
        count = 0

        for i in range(0, n):
            if nums[i] == 0:
                prefix += 1
            else:
                prefix = 0

            count+=prefix

        return count 


            