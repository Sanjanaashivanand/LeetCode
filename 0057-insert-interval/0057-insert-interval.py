class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        res = []
        i = 0

        #Not overlapping in starting 
        while i<n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i+=1

        #string when overlap
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1

        #Insert new interval 
        res.append(newInterval)

        #add left overs 
        while i<n:
            res.append(intervals[i])
            i+=1

        return res