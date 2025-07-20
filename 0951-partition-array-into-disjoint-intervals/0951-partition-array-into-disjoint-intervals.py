class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Largest on the left must be less than the smallest of the right
        n = len(nums)
        left = [0] * n
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = max(left[i-1], nums[i])

        right = [0] * n 
        right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right[i] = min(right[i+1], nums[i])
        
        for i in range(0, n):
            if left[i] <= right[i+1]:
                return i+1
        