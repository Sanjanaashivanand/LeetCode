class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0

        curr_sum = 0
        res = float('inf')

        while j!=len(nums):
            curr_sum+=nums[j]

            while curr_sum>=target:
                res = min(res, j-i+1)
                curr_sum-=nums[i]
                i+=1
            
            j+=1

        return res if res!=float('inf') else 0
                



        