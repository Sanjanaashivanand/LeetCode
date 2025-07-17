class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        prefix = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        MOD = 10**9 + 7

        def helper(idx, prev, dp):
            if idx == n:
                return 1

            if (idx, prev) in dp:
                return dp[(idx, prev)]

            count = 0
            for nxt in prefix[prev]:
                count = (count + helper(idx+1, nxt, dp))%MOD
            
            dp[(idx, prev)] = count
            return count

        count = 0
        dp = {}
        for i in prefix.keys():
            count = (count +  helper(1, i, dp))%MOD

        return count



        

            