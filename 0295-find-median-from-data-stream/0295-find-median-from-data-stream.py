import heapq

class MedianFinder(object):

    def __init__(self):
        self.low = []  # Max heap (invert values to simulate max behavior)
        self.high = [] # Min heap

    def addNum(self, num):
        # Push to max heap (invert value)
        heapq.heappush(self.low, -num)

        # Balance: move largest of low to high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Maintain size invariant
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0
