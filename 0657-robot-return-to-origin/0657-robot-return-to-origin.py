class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        top = 0
        left = 0

        for i in moves:
            if i == 'U':
                top+=1
            elif i == 'D':
                top-=1
            elif i == 'L':
                left +=1
            else:
                left -=1
        
        return top==0 and left==0