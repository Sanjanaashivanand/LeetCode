class Solution(object):
    def shipWithinDays(self, weights, days):
        def canShip(capacity):
            days_needed = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    days_needed += 1
                    current = 0
                current += w
            return days_needed <= days

        low = max(weights)
        high = sum(weights)
        res = high

        while low <= high:
            mid = (low + high) // 2
            if canShip(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
