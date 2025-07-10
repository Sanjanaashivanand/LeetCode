class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        max_freq = defaultdict(int)
        i = 0
        j = 0
        res = 0
        maxf = 0

        while j < len(s):
            max_freq[s[j]] += 1
            maxf = max(maxf, max_freq[s[j]])

            while (j-i+1) - maxf > k:
                max_freq[s[i]] -= 1
                i+=1

            res = max(res, j-i+1)
            j+=1

        return res
            
