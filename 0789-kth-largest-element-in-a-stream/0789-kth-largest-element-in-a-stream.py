class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.stream = []
        heapq.heapify(self.stream)  # Not strictly needed, but good practice

        for num in nums:
            self.add(num)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        elif val > self.stream[0]:  # If val is larger than smallest in heap
            heapq.heappop(self.stream)
            heapq.heappush(self.stream, val)
        return self.stream[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)