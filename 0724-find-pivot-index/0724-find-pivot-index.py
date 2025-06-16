class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)
        curr = 0

        for i,num in enumerate(nums):
            total -= num
            if total - curr == 0:
                return i
            curr += num
            

        return -1