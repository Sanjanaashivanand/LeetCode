class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = -1
        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if num == candidate else -1

        return candidate
        