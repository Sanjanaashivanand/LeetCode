class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()

        available = [i for i in range(n)]
        in_use = [] #(end, room)
        count = [0] * n

        for start, end in meetings:
            #Remove all the meetings that are done
            while in_use and start >= in_use[0][0]:
                _, room = heapq.heappop(in_use)
                heapq.heappush(available, room)

            #If no room available
            if not available:
                end_time, room = heapq.heappop(in_use)
                #Update the end time (new end time of the meeting)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            room = heapq.heappop(available)
            heapq.heappush(in_use, (end, room))
            count[room] += 1

        return count.index(max(count))

