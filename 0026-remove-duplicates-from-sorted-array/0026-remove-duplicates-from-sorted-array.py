class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        count = 0
        
        l = 0
        r = 1

        while l<len(nums)-1 and r<len(nums):
            curr = nums[l]

            while r<len(nums) and nums[r]==curr:
                r+=1
                count+=1

            if r == len(nums):
                break

            #Swap
            temp = nums[l+1]
            nums[l+1] = nums[r]
            nums[r] = nums[l+1]

            l+=1
            r+=1

        return n - count

        