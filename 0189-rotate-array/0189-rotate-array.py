class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        l = 0
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

        l = 0
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

        l = k
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

