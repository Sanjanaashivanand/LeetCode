class Solution(object):
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])  # Sort by end day
        max_heap = []
        time = 0

        for duration, last_day in courses:
            time += duration
            heapq.heappush(max_heap, -duration)
            if time > last_day:
                time += heapq.heappop(max_heap)  # remove longest course

        return len(max_heap)
                
        