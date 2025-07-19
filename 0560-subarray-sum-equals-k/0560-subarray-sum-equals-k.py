class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix = defaultdict(int)
        prefix[0] = 1
        sumSoFar = 0
        count = 0

        for i in range(0,n):
            sumSoFar += nums[i]
            if sumSoFar - k in prefix:
                count += prefix[sumSoFar - k]
            prefix[sumSoFar]+=1
        
        return count
