class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []

        def permute(curr, opened, close):
            if len(curr) == 2*n:
                self.res.append(curr)
                return 
    
            if opened < n:
                permute(curr + '(', opened+1, close)
            if close < opened:
                permute(curr + ')', opened, close+1)

        permute("",0,0)
        return [i for i in self.res]


         