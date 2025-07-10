class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(piles)
        res = float('inf')

        while low<=high:
            banans = (low+high)//2
            time_taken = 0

            for num in piles:
                time_taken += ceil(float(num)/banans)
            

            if time_taken <= h:
                res = min(res, banans)
                high = banans - 1

            else:
                low = banans + 1

        return res

            


