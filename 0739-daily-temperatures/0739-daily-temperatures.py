class Solution(object):
    '''
    temperatures = [73,74,75,71,69,72,76,73]
    [        1 ,1,0, 0]

    [69, 72, 76]
    '''
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)

        stack = []
        stack.append(n-1)
        res = [0] * n
        
        for i in range(n-2, -1, -1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop() 

            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
            

        return res

        

            
        