class Solution(object):
    def minDistance(self, text1, text2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)

        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        def find(idx1, idx2):
            if idx1==m and idx2==n:
                return 0

            if dp[idx1][idx2]!=-1:
                return dp[idx1][idx2]

            #Insert Characters 
            if idx1 == m:
                return n - idx2
            
            #Delete
            if idx2 == n:
                return m - idx1

            res = -1
            #Replace
            if text1[idx1] == text2[idx2]:
                res = find(idx1+1, idx2+1)

            else:
                insert_op = 1 + find(idx1, idx2 + 1)
                delete_op = 1 + find(idx1 + 1, idx2)
                replace_op = 1 + find(idx1 + 1, idx2 + 1)
                res = min(insert_op, delete_op, replace_op)

            dp[idx1][idx2] = res
            return dp[idx1][idx2]

        return find(0,0)
        