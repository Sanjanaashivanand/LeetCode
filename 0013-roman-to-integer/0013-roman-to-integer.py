class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        arr = [0] * len(s)
        for i in range(0, len(s)):
            arr[i] = map[s[i]]

        print(arr)
        res = 0
        for i in range(len(arr)-1, -1, -1):
            if i!=len(arr)-1 and arr[i+1]>arr[i]:
                res-=arr[i]
            else:
                res+=arr[i]
        
        return res