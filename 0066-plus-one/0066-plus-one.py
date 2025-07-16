class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carryOver = True

        for i in range(n - 1, -1, -1):
            total = digits[i] + (1 if carryOver else 0)
            
            if total > 9:
                carryOver = True
                digits[i] = 0

            else:
                carryOver = False
                digits[i] = total

            if carryOver == False:
                return digits
        
        return [1] + digits