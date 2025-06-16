class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for ast in asteroids:

            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    not_destroyed = False
                break
            
            else: 
                stack.append(ast)

        return stack
            

                

                    
            
        return stack


            