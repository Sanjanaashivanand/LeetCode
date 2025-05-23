class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0: return False

        check = set([2, 3, 4, 5, 7])
        num = ""
        copy = n
        
        flag = 0
        while(n!=0):
            dig = n%10

            if dig == 9:
                num += str(6)
            elif dig == 6:
                num += str(9)
            else:
                num += str(dig)
            

            if dig in check:
                return False
            n = n // 10

        if flag == 1:
            return True

        if int(num)!=copy:
            return True
        
        return False
        