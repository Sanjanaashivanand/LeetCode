class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if s[i] == '*' else 0)
        print(prefix)
        left_candle = [-1] * n
        last = -1
        for i in range(0, n):
            if s[i] == '|':
                last = i
            left_candle[i] = last

        right_candle = [-1] * n 
        right = -1
        for i in range(n-1, -1, -1):
            if s[i]=='|':
                right=i 
            right_candle[i] = right

        res = []
        for left, right in queries:
            l = right_candle[left]
            r = left_candle[right]
        
            if l != -1 and r != -1 and l <= r:
                res.append(prefix[r] - prefix[l])
            else:
                res.append(0)

        return res
