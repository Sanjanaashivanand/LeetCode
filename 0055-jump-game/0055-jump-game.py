class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
  
        goal = n-1
        i = n-1

        while i>=0:
            if i + nums[i] >= goal:
                goal = i 
            i-=1 
        
        return goal == 0