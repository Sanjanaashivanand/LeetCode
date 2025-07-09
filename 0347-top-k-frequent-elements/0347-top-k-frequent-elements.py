class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)

        sort_count = sorted(count, key = lambda x: count[x], reverse=True)

        res = []
        
        for key in sort_count:
            res.append(key)
            if len(res) == k:
                break

        return res
            
            