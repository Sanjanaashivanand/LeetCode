class Solution(object):
    def maxCoins(self, nums):
        n = len(nums)
        memo = {}

        def helper(picked):
            if len(picked) == n:
                return 0

            key = frozenset(picked)
            if key in memo:
                return memo[key]

            max_coins = 0

            for idx in range(n):
                if idx in picked:
                    continue

                l = idx - 1
                while l >= 0 and l in picked:
                    l -= 1

                r = idx + 1
                while r < n and r in picked:
                    r += 1

                left = nums[l] if l >= 0 else 1
                right = nums[r] if r < n else 1

                picked.add(idx)
                coins = left * nums[idx] * right + helper(picked)
                picked.remove(idx)

                max_coins = max(max_coins, coins)

            memo[key] = max_coins
            return max_coins

        return helper(set())
