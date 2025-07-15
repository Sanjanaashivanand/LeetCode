class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        res = stones[1] - stones[0]

        for i in range(2, n, 2):
            res = max(res, stones[i] - stones[i-2])

        for i in range(3, n, 2):
            res = max(res, stones[i] - stones[i-2])      

        return res    