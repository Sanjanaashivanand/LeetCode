class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        n = len(nums)

        while i < n:
            correct = nums[i] - 1

            if nums[i] <= n and nums[i] > 0 and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i+=1
        
        for i in range(0, n):
            if i+1 != nums[i]:
                return i+1 

        return n+1





                    

            
            
        print(nums)