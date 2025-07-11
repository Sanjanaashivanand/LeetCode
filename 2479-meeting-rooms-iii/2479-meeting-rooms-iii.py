class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings = sorted(meetings, key = lambda x:x[0])

        room_availability_time = [0] * n
        meeting_count = [0] * n

        for start, end in meetings:

            min_room_availabity_time = float('inf')
            min_available_room = 0

            found_room = False

            for i in range (0, n):
                if room_availability_time[i] <= start:
                    room_availability_time[i] = end
                    meeting_count[i] += 1
                    found_room = True
                    break

                if room_availability_time[i] < min_room_availabity_time:
                    min_room_availabity_time = room_availability_time[i]
                    min_available_room = i 

            if not found_room:
                room_availability_time[min_available_room] += end - start
                meeting_count[min_available_room] += 1

        res = 0

        for i in range(n):
            if meeting_count[i] > meeting_count[res]:
                res = i 

        return res

                
