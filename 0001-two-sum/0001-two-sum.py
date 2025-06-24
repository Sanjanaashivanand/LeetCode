class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in hash:
                return [hash[diff], i]
            hash[nums[i]] = i

        return [-1.-1]
        