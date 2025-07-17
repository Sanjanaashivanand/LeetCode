class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n-2
        
        #Find the first dip
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot>=0:
            nxt = len(nums) - 1
            while nums[nxt] <= nums[pivot]:
                nxt-=1
            nums[pivot], nums[nxt] = nums[nxt], nums[pivot]
        
        left = pivot+1
        right = n-1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

            

