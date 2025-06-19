class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        res = high

        while low<=high:
            mid = (low+high)//2
            print("Mid " , mid)

            time_taken = 0

            for bananas in piles:
                time_taken += math.ceil(float(bananas) / mid)
                if time_taken > h:
                    break

            if int(time_taken) <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1

        return res