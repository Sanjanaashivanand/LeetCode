class Solution:
    def partitionString(self, s: str) -> int:
        curr = ""
        i = 0
        count = 0

        while i<len(s):
            if s[i] in curr:
                count += 1
                curr = ""
            curr+=s[i]
            i+=1

        count += 1
        return count
            
