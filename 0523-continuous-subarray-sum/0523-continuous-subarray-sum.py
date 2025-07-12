from collections import defaultdict

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix = {0: -1}  # remainder -> index
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            rem = curr_sum % k if k != 0 else curr_sum

            if rem in prefix:
                if i - prefix[rem] >= 2:
                    return True
            else:
                prefix[rem] = i  # store only the first occurrence

        return False
