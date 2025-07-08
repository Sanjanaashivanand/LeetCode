class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        def helper(length, dp):
            if length > high:
                return 0

            if dp[length]!=-1:
                return dp[length]

            count = 1 if low <= length <= high else 0
            count += helper(length+one, dp) % (10**9 + 7)
            count += helper(length+zero, dp) % (10**9 + 7)
            dp[length] = count % (10**9 + 7)
            return count
       

        dp = [-1 for _ in range(high+1)]
        helper(0, dp)
        return dp[0]

            
                
