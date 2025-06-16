class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0

        ones = 0
        zeros = 0

        res = 0

        while j < len(nums):

            while j<len(nums):
                if nums[j] == 1:
                    ones+=1
                elif zeros!=1:
                    zeros+=1
                else:
                    break
                j+=1

            if zeros == 1:
                res = max(res, ones)
            else:
                res = max(res, ones-1)

            if nums[i] == 0:
                zeros = 0
            else:
                ones -= 1
            i+=1

        return res
