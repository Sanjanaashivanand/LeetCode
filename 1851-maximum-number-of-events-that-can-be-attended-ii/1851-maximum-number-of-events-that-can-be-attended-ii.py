class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort()  # Sort by start time
        n = len(events)

        # Initialize dp table: dp[i][left] = max value using events[i:] with 'left' choices
        dp = [[-1] * (k + 1) for _ in range(n)]

        def find_next(i, events):
            lo = i + 1
            hi = len(events)
            target = events[i][1]

            while lo < hi:
                mid = (lo + hi) // 2
                if events[mid][0] > target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        def helper(i, left):
            if i == n or left == 0:
                return 0

            if dp[i][left] != -1:
                return dp[i][left]

            # ✅ Corrected: Pass full events, not sliced
            next_i = find_next(i, events)

            # Option 1: pick the current event
            pick = events[i][2] + helper(next_i, left - 1)

            # Option 2: skip the current event
            skip = helper(i + 1, left)

            dp[i][left] = max(pick, skip)
            return dp[i][left]

        return helper(0, k)
