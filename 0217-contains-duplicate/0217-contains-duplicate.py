class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set()

        for i in nums:
            if i in unique:
                return True
            unique.add(i)

        return False