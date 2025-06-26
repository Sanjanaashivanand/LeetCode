class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        right = len(nums) - 1
        count = 0

        while right>=0 and nums[right] == val:
            right -= 1
            count+=1

        left = 0
        while left<right:
            if nums[left] == val:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                while right>=0 and nums[right] == val:
                    right -= 1
                    count+=1
            left+=1
        
        return len(nums) - count 