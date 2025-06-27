
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""

        strs.sort()

        for i in range(0, len(strs[0])):
            curr = strs[0][i]
            for j in range(1, len(strs)):
                if curr != strs[j][i]:
                    return common
            
            common += curr
    

        return common