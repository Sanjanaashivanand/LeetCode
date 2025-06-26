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
            new_goal = goal
            for j in range(goal-1, -1, -1):
                if j + nums[j] >= goal:
                    new_goal = j

            if goal != new_goal:
                goal = new_goal
                jumps+=1
        
        return jumps

        