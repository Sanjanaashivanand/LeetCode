class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[1])

        count = 1
        prev = 0

        for i in range(1, n):
            if  intervals[prev][1] <= intervals[i][0]:
                count+=1
                prev = i

        return n-count



        