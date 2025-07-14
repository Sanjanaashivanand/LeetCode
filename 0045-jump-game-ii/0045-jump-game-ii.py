class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        goal = n-1
        jumps = 0
        
        while goal>0:
            for i in range(0, n):
                if i + nums[i] >= goal:
                    goal = i 
                    jumps+=1
                    break 

        return jumps
            
