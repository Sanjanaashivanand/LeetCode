import bisect

class Solution(object):
    def maxEnvelopes(self, envelopes):
        # Step 1: Sort by width ASC, height DESC
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Step 2: Extract heights
        heights = [h for w, h in envelopes]

        # Step 3: Find LIS on heights
        dp = []
        for h in heights:
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h

        return len(dp)
