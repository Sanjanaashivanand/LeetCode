class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        al = 0
        res = -1
        for i in gain:
            al += i
            res = max(res, al)
        return 0 if res<0 else res
