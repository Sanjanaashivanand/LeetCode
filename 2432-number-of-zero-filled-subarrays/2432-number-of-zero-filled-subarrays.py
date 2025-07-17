class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * n
        prefix[0] = 1 if nums[0]==0 else 0

        for i in range(1, n):
            if nums[i] == 0:
                prefix[i] = max(1, prefix[i-1]+1)

        return sum(prefix)


            