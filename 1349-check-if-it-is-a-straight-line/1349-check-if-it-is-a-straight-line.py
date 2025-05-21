class Solution(object):
    def checkStraightLine(self, cord):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(cord) <= 1:
            return False
        if len(cord) == 2:
            return True

        x0, y0 = cord[0]
        x1, y1 = cord[1]
        dx = x1 - x0
        dy = y1 - y0

        for i in range(2, len(cord)):
            xi, yi = cord[i]
            if dy * (xi - x0) != dx * (yi - y0):
                return False

        return True