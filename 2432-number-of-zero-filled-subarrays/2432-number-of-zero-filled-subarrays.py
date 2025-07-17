class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 0
        count = 0

        for num in nums:
            if num == 0:
                prefix += 1
            else:
                prefix = 0

            count+=prefix

        return count 


            