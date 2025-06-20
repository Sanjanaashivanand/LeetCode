class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        n = len(points)
        points = sorted(points, key = lambda x : x[1])

        first_end = points[0][1]
        count = 1

        for x_start, x_end in points:
            if first_end < x_start:
                count += 1
                first_end = x_end

        return count
        