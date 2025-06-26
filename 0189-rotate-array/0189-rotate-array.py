class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        #Reverse Entire Array
        l = 0
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

        #Reverse first half
        l = 0
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

        #Reverse second half
        l = k
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

