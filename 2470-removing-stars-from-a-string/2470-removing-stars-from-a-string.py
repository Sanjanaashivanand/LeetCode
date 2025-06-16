class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else: 
                stack.append(i)
        
        stack = stack[::-1]
        s = ""
        while len(stack)!=0:
            s += stack.pop()
        return s
        