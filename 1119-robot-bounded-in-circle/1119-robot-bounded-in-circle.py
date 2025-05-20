class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        pos = [0, 0]
        turns = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr = 0

        for i in instructions:
            if i == 'G':
                pos[0] += turns[curr][0]
                pos[1] += turns[curr][1]
            elif i == 'L':
                curr = (curr + 3) % 4  # Turn Left
            else:  # 'R'
                curr = (curr + 1) % 4  # Turn Right
        
        return (pos[0] == 0 and pos[1] == 0) or curr != 0
        

        