class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        count = 0
        min_pos = -1  # last position of minK
        max_pos = -1  # last position of maxK
        left_bound = -1  # last position of invalid number

        for r, val in enumerate(nums):
            if val < minK or val > maxK:
                left_bound = r  # reset the window
            if val == minK:
                min_pos = r
            if val == maxK:
                max_pos = r

            # count subarrays ending at r with both minK and maxK in them
            count += max(0, min(min_pos, max_pos) - left_bound)

        return count
