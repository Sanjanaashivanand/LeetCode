class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        def helper(idx, sumSoFar, dp):
            if idx==n:
                if sumSoFar == target:
                    return 1
                return 0

            if (idx, sumSoFar) in dp:
                return dp[(idx, sumSoFar)]

            #Add
            add = helper(idx+1, sumSoFar+nums[idx], dp)

            #Subtract
            sub = helper(idx+1, sumSoFar-nums[idx], dp)
            
            dp[(idx, sumSoFar)] = add + sub
            return add + sub 

        dp = {}
        return helper(0, 0, dp)