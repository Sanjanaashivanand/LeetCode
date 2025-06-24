class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 0
            count[i]+=1

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        print(sorted_items)

        res=[]

        for i in range(k):
            res.append(sorted_items[i][0])
        
        return res
        