class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        goal = len(nums) - 1
        jumps = 0

        while goal>0:
            for i in range(goal):
                if i + nums[i] >= goal:
                    goal = i
                    jumps+=1   
                    break 
        
        return jumps

        