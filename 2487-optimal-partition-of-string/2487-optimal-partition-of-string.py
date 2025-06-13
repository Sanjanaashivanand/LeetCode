class Solution:
    def partitionString(self, s: str) -> int:
        curr = set()
        i = 0
        count = 0

        while i<len(s):
            if s[i] in curr:
                count += 1
                curr.clear()
            curr.add(s[i])
            i+=1

        count += 1
        return count
            
