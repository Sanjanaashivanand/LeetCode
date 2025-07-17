class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 0
        j = 0

        minSoFar = [0] * n
        maxSoFar = [0] * n

        minSoFar[0] = nums[0]
        maxSoFar[-1] = nums[-1]

        for i in range(1,n):
            minSoFar[i] = min(nums[i], minSoFar[i-1])
            maxSoFar[n-i-1] = max(nums[n-i-1], maxSoFar[n-i])
        
        for i, num in enumerate(nums):
            if minSoFar[i] < num < maxSoFar[i]:
                return True 

        return False

            
