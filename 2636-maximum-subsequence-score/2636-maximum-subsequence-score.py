class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs = [(x,y) for x,y in zip(nums1,nums2)]
        pairs = sorted(pairs, key = lambda x : x[1], reverse=True)
        
        min_heap = []
        curr_sum = 0
        max_score = -1

        for num1, num2 in pairs:
            heappush(min_heap, num1)
            curr_sum += num1

            if len(min_heap) > k:
                curr_sum -= heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(max_score, (curr_sum * num2))
                
        return max_score






            


            


        