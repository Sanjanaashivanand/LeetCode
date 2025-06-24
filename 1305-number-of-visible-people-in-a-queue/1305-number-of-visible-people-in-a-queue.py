class Solution(object):
    def canSeePersonsCount(self, heights):
        n = len(heights)
        res = [0] * n
        stack = []  # store indices of people
        
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                count += 1
            if stack:
                count += 1  # can see the next taller one
            res[i] = count
            stack.append(i)
            
        return res

