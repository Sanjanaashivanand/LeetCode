class Solution:
    def partitionString(self, s: str) -> int:
        curr = [0] * 26
        i = 0
        count = 0

        while i<len(s):
            if curr[ord(s[i]) - ord('a')] == 1:
                count += 1
                curr = [0] * 26
            curr[ord(s[i]) - ord('a')] = 1
            i+=1

        count += 1
        return count
            
