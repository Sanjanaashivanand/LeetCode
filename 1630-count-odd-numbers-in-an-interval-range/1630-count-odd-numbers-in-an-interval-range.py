class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low%2==0: 
            low+=1

        return 0 if low > high else (high - low)/2 + 1