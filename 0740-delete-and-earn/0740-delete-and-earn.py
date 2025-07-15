class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        hashmap = Counter(nums)
        unique = sorted(set(nums))  # Fix 1: sort unique values

        n = len(unique)
        dp = [0] * n
        dp[0] = unique[0] * hashmap[unique[0]]

        if n == 1:
            return dp[0]

        if unique[1] == unique[0] + 1:
            dp[1] = max(dp[0], unique[1] * hashmap[unique[1]])
        else:
            dp[1] = dp[0] + unique[1] * hashmap[unique[1]]

        for i in range(2, n):
            curr = unique[i] * hashmap[unique[i]]
            if unique[i] == unique[i - 1] + 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + curr)
            else:
                dp[i] = dp[i - 1] + curr

        return dp[-1]