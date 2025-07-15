class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        total = sum(nums)

        def helper(idx, sumSoFar, memo):
            if idx == n:
                return False

            if (idx, sumSoFar) in memo:
                return memo[(idx, sumSoFar)]

            if sumSoFar == total - sumSoFar:
                return True

            #Pick 
            if helper(idx+1, sumSoFar+nums[idx], memo):
                memo[(idx, sumSoFar)] = True
                return True

            #Not Pick
            if helper(idx+1, sumSoFar, memo):
                memo[(idx, sumSoFar)] = True
                return True
            
            memo[(idx, sumSoFar)] = False
            return False


        memo = {}
        return helper(0, 0, memo)
        