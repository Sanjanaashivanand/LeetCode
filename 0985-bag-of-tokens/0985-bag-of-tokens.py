class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        n = len(tokens)
        score = 0
        i = 0
        j = n-1

        while i<=j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                i+=1
            elif i<j and score >= 1:
                power += tokens[j]
                score -= 1
                j-=1
            else:
                return score

        return score