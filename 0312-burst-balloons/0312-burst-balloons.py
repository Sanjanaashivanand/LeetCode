class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr = [0] * (n+2)
        arr[0] = arr[n+1] = 1

        for i in range(0, n):
            arr[i+1] = nums[i]

        def burst(left, right):
            if left+1 == right:
                return 0

            if (left, right) in dp:
                return dp[(left, right)]

            maxi = 0

            for i in range(left+1, right):
                maxi = max(maxi, arr[left] * arr[i] * arr[right] + burst(left, i) + burst(i, right))
            
            dp[(left, right)] = maxi
            return maxi

        dp = {}
        return burst(0, n+1)