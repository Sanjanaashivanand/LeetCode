class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = [0] * 26 

        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i 

        size = 0
        last_idx = 0
        res = []

        for i ,c in enumerate(s):
            last_idx = max(last[ord(c) - ord('a')], last_idx)
            size += 1
            
            if i == last_idx:
                res.append(size)
                size = 0


        return res

        