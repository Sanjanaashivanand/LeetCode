class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        slow = 0
        fast = 1

        while fast<n:
            if nums[slow] == nums[fast]:
                fast+=1
            else:
                nums[slow+1] = nums[fast]
                slow+=1
                fast+=1
        return slow+1

        