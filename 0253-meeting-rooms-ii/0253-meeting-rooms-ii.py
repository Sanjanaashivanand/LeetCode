class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])  # Sort by start time

        heap = []
        heapq.heappush(heap, intervals[0][1])  # Push end time of first meeting

        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i][0]:  # Room is free
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])  # Add current meeting's end time

        return len(heap)


