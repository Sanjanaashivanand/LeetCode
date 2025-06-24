class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = set()
        for i in nums:
            if i in hash:
                return True
            hash.add(i)

        return False
        