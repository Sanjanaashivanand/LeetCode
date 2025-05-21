class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = tens = twenties = 0
        for i in bills:
            if i == 5:
                fives+=1
            elif i == 10:
                tens += 1
                if fives <= 0:
                    return False
                fives -= 1
            else:
                twenties += 1
                if tens <= 0:
                    if fives >= 3:
                        fives -= 3
                    else:
                        return False
                else:
                    tens -= 1
                    if fives <= 0:
                        return False
                    fives -= 1
            
        return True