class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        heap = []

        for key in count:
            heappush(heap, (count[key], key))
            if len(heap) > k:
                heappop(heap) 

        return [item[1] for item in heap]  
            
            